from django.urls import path

from .views import *

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
    # CATEGORY
    path('category/list/', CategoryView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/toggle/<int:pk>/', categoryToggle, name='category_toggle'),

    # SUBCATEGORY
    path('subcategory/list/', SubCategoryView.as_view(), name='subcategory_list'),
    path('subcategory/create/', SubCategoryCreate.as_view(), name='subcategory_create'),
    path('subcategory/update/<int:pk>/', SubCategoryUpdate.as_view(), name='subcategory_update'),
    path('subcategory/toggle/<int:pk>/', subcategoryToggle, name='subcategory_toggle'),
    
    # BRAND
    path('brand/list/', BrandView.as_view(), name='brand_list'),
    path('brand/create/', BrandCreate.as_view(), name='brand_create'),
    path('brand/update/<int:pk>/', BrandUpdate.as_view(), name='brand_update'),
    path('brand/toggle/<int:pk>/', brandToggle, name='brand_toggle'),
    
]
