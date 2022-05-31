from pipes import Template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView, View, FormView, DetailView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

from social.models import Post

from users.models import Profile

from django.contrib.sites.shortcuts import get_current_site

from django.template.loader import render_to_string

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.utils.encoding import *

from django.core.mail import EmailMessage

from django.conf import settings

from .forms import *

from .utils import *

import threading


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

# Create your views here.
class Register(FormView):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('home')
    
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(*args, **kwargs)
        
    def form_valid(self, form):
        user = form.save()
        send_verify_email(user, self.request)
        return super().form_valid(form) 
    
def send_verify_email(user, request):
    current_site = get_current_site(request)
    subject = 'Verificación de correo electrónico'
    body = render_to_string('users/verify_email.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user),
        })
    email = EmailMessage(subject, body, from_email=settings.EMAIL_NAME, to=[user.user.email])
    
    EmailThread(email).start()
    
def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        print(uid)
        user = Profile.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and generate_token.check_token(user, token):
        user.is_verify = True
        user.save()
        return redirect('home')  
    return render(request, 'users/activate_error_user.html', {})
    
class ProfileView(LoginRequiredMixin, DetailView):

    template_name = 'users/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(profile__user=user).order_by('-created')
        return context

class ProfileEdit(LoginRequiredMixin, UpdateView):
    
    model = Profile
    template_name = 'users/settings.html'
    fields = ['website', 'twitter', 'instagram', 'facebook', 'bio', 'phone', 'organization', 'location', 'gender', 'picture', 'color_primary', 'color_secondary']

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        username = self.object.user.username
        return reverse_lazy('users:settings')
        # return reverse_lazy('users:profiles', kwargs={'username': username})


class UserEdit(LoginRequiredMixin, UpdateView):
    
    template_name = 'users/settings_user.html'
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:settings')