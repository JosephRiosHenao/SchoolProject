from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.http import HttpResponse

from inventory.models import *
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


class BuyView(LoginRequiredMixin, ListView):
    model = BuyHead
    context_object_name = 'obj'
    template_name = 'cmp/buy_list.html'
    
    def get_queryset(self): return BuyHead.objects.filter(user_created = self.request.user)
    

def buy(request, id_buy=None):
    template_name = 'cmp/buy.html'
    products = Product.objects.filter(user_created = request.user)
    form_buy = {}
    context = {}
    if request.method == "GET":
        form_buy = BuyForm()
        obj = BuyHead.objects.filter(pk=id_buy).first()
        
        if obj:
            details = BuyData.objects.filter(buy_head=obj)
            date_buy = datetime.time.isoformat(obj.date_buy)
            date_fact = datetime.time.isoformat(obj.date_fact)
            e = {
                "date_buy": date_buy,
                "date_fact": date_fact,
                "provider": obj.provider,
                "observation": obj.observation,
                "no_fact": obj.no_fact,
                "sub_total": obj.sub_total,
                "offert": obj.offert,
                "total": obj.total,
            }
            
            form_buy = BuyForm(e)
        else: details = None
        
        context = {
            "products": products,
            "buy": obj,
            "details": details,
            "form_buy": form_buy,
        }
        
        return render(request, template_name, context)
    