from django.urls import path

from .views import *

urlpatterns = [
    path('', ListsPosts.as_view(), name='feed'),
    path('create/', CreatePost.as_view(), name='create_post'),
    path('<int:pk>/', DetailPost.as_view(), name='detail_post'),
]
