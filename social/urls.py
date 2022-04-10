from django.urls import path

from .views import *

urlpatterns = [
    path('', ListsPosts.as_view(), name='feed'),
    path('create', CreatePost.as_view(), name='create'),
    path('<int:pk>', DetailPost.as_view(), name='detail'),
    path('api/toggle', togglePost , name="toggle"),
]
