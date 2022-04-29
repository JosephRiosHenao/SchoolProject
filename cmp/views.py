from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import *
from .forms import *

# Create your views here.

class ProviderView(LoginRequiredMixin, ListView):
    model = Provider
    context_object_name = 'obj'
    template_name = 'cmp/provider_list.html'
    
    def get_queryset(self): return Provider.objects.filter(user_created = self.request.user)
    
class ProviderCreateView(LoginRequiredMixin, CreateView):
    model = Provider
    form_class = ProviderForm
    template_name = 'cmp/provider_form.html'
    success_url = reverse_lazy('cmp:provider_list')

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        form.instance.user_modified = self.request.user
        return super().form_valid(form)

class ProviderUpdateView(LoginRequiredMixin, UpdateView):
    model = Provider
    form_class = ProviderForm
    context_object_name = 'obj'
    template_name = 'cmp/provider_form.html'
    success_url = reverse_lazy('cmp:provider_list')
    
    def form_valid(self, form):
        form.instance.user_modified = self.request.user
        return super().form_valid(form)
    
def providerToggle(request, pk):
    provider = Provider.objects.get(pk=pk)
    provider.state = not provider.state
    provider.save()
    return redirect('cmp:provider_list')