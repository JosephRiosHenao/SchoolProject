from django.urls import path

from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name="users/login.html", redirect_authenticated_user = True), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name="users/login.html"), name='logout'),
    path('register', Register.as_view(), name='register'),
    path('settings', ProfileEdit.as_view(), name='settings'),
    path('<str:username>', ProfileView.as_view(), name='profiles'), # No terminado view ni template logic
    path('activate-user/<uidb64>/<token>', activate_user, name='activate'),
]