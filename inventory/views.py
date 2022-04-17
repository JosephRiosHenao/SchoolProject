from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

from .form import *

# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/dashboard.html'
    
    
# CATEGORY
    
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

def categoryToggle(request, pk):
    category = Category.objects.get(pk=pk)
    category.state = not category.state
    category.save()
    return redirect('inventory:category_list')

# SUBCATEGORY

class SubCategoryView(LoginRequiredMixin, ListView):
    model = SubCategory
    context_object_name = 'obj'
    template_name = 'inventory/subcategory_list.html'
    
class SubCategoryCreate(LoginRequiredMixin, CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'inventory/subcategory_form.html'
    success_url = reverse_lazy('inventory:subcategory_list')
    
    def form_valid(self, form):
        form.instance.user_created = self.request.user
        form.instance.user_modified = self.request.user
        return super().form_valid(form)

class SubCategoryUpdate(LoginRequiredMixin, UpdateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'inventory/subcategory_form.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inventory:subcategory_list')
    
    def form_valid(self, form):
        form.instance.user_modified = self.request.user
        return super().form_valid(form)
    
def subcategoryToggle(request, pk):
    subcategory = SubCategory.objects.get(pk=pk)
    subcategory.state = not subcategory.state
    subcategory.save()
    return redirect('inventory:subcategory_list')
    
    
# BRAND

class BrandView(LoginRequiredMixin, ListView):
    model = Brand
    context_object_name = 'obj'
    template_name = 'inventory/brand_list.html'

class BrandCreate(LoginRequiredMixin, CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'inventory/brand_form.html'
    success_url = reverse_lazy('inventory:brand_list')
    
    def form_valid(self, form):
        form.instance.user_created = self.request.user
        form.instance.user_modified = self.request.user
        return super().form_valid(form)

class BrandUpdate(LoginRequiredMixin, UpdateView):
    model = Brand
    form_class = BrandForm
    context_object_name = 'obj'
    template_name = 'inventory/brand_form.html'
    success_url = reverse_lazy('inventory:brand_list')
    
    def form_valid(self, form):
        form.instance.user_modified = self.request.user
        return super().form_valid(form)
    
def brandToggle(request, pk):
    brand = Brand.objects.get(pk=pk)
    brand.state = not brand.state
    brand.save()
    return redirect('inventory:brand_list')


class UnitMeterView(LoginRequiredMixin, ListView):
    model = UnitMeter
    context_object_name = 'obj'
    template_name = 'inventory/unitmeter_list.html'

class UnitMeterCreate(LoginRequiredMixin, CreateView):
    model = UnitMeter
    form_class = UnitMeterForm
    template_name = 'inventory/unitmeter_form.html'
    success_url = reverse_lazy('inventory:unitmeter_list')

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        form.instance.user_modified = self.request.user
        return super().form_valid(form)

class UnitMeterUpdate(LoginRequiredMixin, UpdateView):
    model = UnitMeter
    context_object_name = 'obj'
    form_class = UnitMeterForm
    template_name = 'inventory/unitmeter_form.html'
    success_url = reverse_lazy('inventory:unitmeter_list')
    
    def form_valid(self, form):
        form.instance.user_modified = self.request.user
        return super().form_valid(form)
    
def unitmeterToggle(request, pk):
    unitmeter = UnitMeter.objects.get(pk=pk)
    unitmeter.state = not unitmeter.state
    unitmeter.save()
    return redirect('inventory:unitmeter_list')

class ProductView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'obj'
    template_name = 'inventory/product_list.html'

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('inventory:product_list')
    
    def form_valid(self, form):
        form.instance.user_created = self.request.user
        form.instance.user_modified = self.request.user
        return super().form_valid(form)

class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'obj'
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('inventory:product_list')
    
    def form_valid(self, form):
        form.instance.user_modified = self.request.user
        return super().form_valid(form)
    
def productToggle(request, pk):
    product = Product.objects.get(pk=pk)
    product.state = not product.state
    product.save()
    return redirect('inventory:product_list')