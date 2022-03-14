from pipes import Template
from django.shortcuts import render

from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(LoginRequiredMixin, TemplateView): 
    template_name = "bases/home.html"
    login_url = 'bases:login'


class Login(TemplateView): 
    template_name = "bases/login.html"

class Register(TemplateView):
    template_name = "bases/register.html"