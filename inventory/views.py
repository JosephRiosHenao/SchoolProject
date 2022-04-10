from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category, SubCategory

from .form import CategoryForm, SubCategoryForm

# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/dashboard.html'
    
class CategoryView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'obj'
    template_name = 'inventory/category_list.html'

class CategoryCreateView(LoginRequiredMixin, CreateView):    
    model = Category
    template_name = 'inventory/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('inventory:category_list')
    
    def form_valid(self, form):
        form.instance.user_created = self.request.user
        form.instance.user_modified = self.request.user
        return super().form_valid(form)
    
class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    context_object_name = 'obj'
    template_name = 'inventory/category_form.html'
    success_url = reverse_lazy('inventory:category_list')
    
    def form_valid(self, form):
        form.instance.user_modified = self.request.user
        return super().form_valid(form)


class SubCategoryView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'obj'
    template_name = 'inventory/subcategory_list.html'
    
class SubCategoryCreate(LoginRequiredMixin, CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'inventory/subcategory_create.html'
    success_url = reverse_lazy('inventory:subcategory_list')
    
    def form_valid(self, form):
        form.instance.user_created = self.request.user
        form.instance.user_modified = self.request.user
        return super().form_valid(form)

class SubCategoryUpdate(LoginRequiredMixin, UpdateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'inventory/subcategory_update.html'
    success_url = reverse_lazy('inventory:subcategory_list')
    
    def form_valid(self, form):
        form.instance.user_modified = self.request.user
        return super().form_valid(form)