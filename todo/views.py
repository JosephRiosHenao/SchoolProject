from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import *
from .forms import *

# Create your views here.
class CreateTodo(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TodoForm
    template_name = "todo/form.html"
    success_url = reverse_lazy("todo:list")
    
    def form_valid(self, form):
        form.instance.user_created = self.request.user
        form.instance.user_modified = self.request.user
        return super().form_valid(form)

class ListTodo(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/list.html"
    
    def get_queryset(self): return Task.objects.filter(user_created=self.request.user)
    
    
class UpdateTodo(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TodoForm
    template_name = 'todo/form.html'
    context_object_name = "obj"
    success_url = reverse_lazy("todo:list")

    def form_valid(self, form):
        form.instance.user_modified = self.request.user
        return super().form_valid(form)


def taskToggle(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('todo:list')