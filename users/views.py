from pipes import Template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView, View, FormView, DetailView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

from social.models import Post

from users.models import Profile

from .forms import *

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
        form.save()
        return super().form_valid(form) 
    
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
    
    template_name = 'users/settings.html'
    model = Profile
    fields = ['website', 'twitter', 'instagram', 'facebook', 'bio', 'phone', 'organization', 'location', 'gender', 'picture']

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