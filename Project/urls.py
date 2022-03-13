from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("apps.home.urls"), name="home"),
    path('register', include("apps.register.urls"), name="register"),
    path('login', include("apps.login.urls"), name="login"),
    path('admin/', admin.site.urls),
]
