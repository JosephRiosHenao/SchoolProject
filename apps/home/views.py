from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, TemplateView
# Create your views here.
class Home(TemplateView):
    template_name = "home/index.html"