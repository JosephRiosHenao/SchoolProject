from django.urls import path

from .views import *

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
    # CATEGORY
    path('category/list/', CategoryView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),

    # SUBCATEGORY
    path('subcategory/list/', SubCategoryView.as_view(), name='subcategory_list'),
    path('subcategory/create/', SubCategoryCreate.as_view(), name='subcategory_create'),
    path('subcategory/update/<int:pk>/', SubCategoryUpdate.as_view(), name='subcategory_update'),
    
]
