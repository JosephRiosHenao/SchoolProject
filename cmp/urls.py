from django.urls import path

from .views import *

urlpatterns = [
    
    # PROVIDER
    path('provider/list/', ProviderView.as_view(), name='provider_list'),
    path('provider/create/', ProviderCreateView.as_view(), name='provider_create'),
    path('provider/update/<int:pk>', ProviderUpdateView.as_view(), name='provider_update'),
    path('provider/toggle/<int:pk>', providerToggle, name='provider_toggle'),
    
    # BUY
    path('buy/list/', BuyView.as_view(), name='buy_list'),
    path('buy/create/', buy, name='buy_create'),
    path("buy/update/<int:id_buy>/", buy, name="buy_update"),

]