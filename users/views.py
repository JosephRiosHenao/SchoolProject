from pipes import Template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView, View, FormView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

from django.db.utils import IntegrityError

from users.models import Profile

from .forms import *

# Create your views here.

# class Register(View):
    
#     template_name = "users/register.html"
#     form_class = RegisterForm
#     redirect_authenticated_user = True
    
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name)
    
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             try:
#                 user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#             except IntegrityError:
#                 return render(request, self.template_name, {'form': form, 'error': 'El usuario ya existe'})
            
#             user.first_name = form.cleaned_data['name']
#             user.last_name = form.cleaned_data['last_name']
#             user.email = form.cleaned_data['email']
#             user.save()
#             profile = Profile.objects.create(user=user)
#             print("Usuario creado")
            
#             return redirect('users:login')
            
#         return render(request, self.template_name, {'form': form})
    
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