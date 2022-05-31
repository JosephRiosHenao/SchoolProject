from django.urls import path

from .views import *

urlpatterns = [
    path('', ListTodo.as_view(), name='list'),
    path('create', CreateTodo.as_view(), name="create"),
    path('<int:pk>', UpdateTodo.as_view(), name='update'),
    path('api/delete/<int:pk>', taskToggle, name="delete"),
]