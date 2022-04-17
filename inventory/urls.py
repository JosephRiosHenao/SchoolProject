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
    
    # UNIT METER
    path('unitmeter/list/', UnitMeterView.as_view(), name='unitmeter_list'),
    path('unitmeter/create/', UnitMeterCreate.as_view(), name='unitmeter_create'),
    path('unitmeter/update/<int:pk>/', UnitMeterUpdate.as_view(), name='unitmeter_update'),
    path('unitmeter/toggle/<int:pk>/', unitmeterToggle, name='unitmeter_toggle'),
    
    # PRODUCT
    path('product/list/', ProductView.as_view(), name='product_list'),
    path('product/create', ProductCreate.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdate.as_view(), name='product_update'),
    path('product/toggle/<int:pk>/', productToggle, name='product_toggle'),
    
]
