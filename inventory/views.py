from django.shortcuts import render

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category

from .form import CategoryForm

# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/dashboard.html'
    
class CategoryView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'obj'
    template_name = 'inventory/category_list.html'

class CategoryCreateView(LoginRequiredMixin, CreateView):    
    model = Category
    template_name = 'inventory/category_create.html'
    form_class = CategoryForm
    
    