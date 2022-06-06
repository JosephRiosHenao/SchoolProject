from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.http import HttpResponse

from django.db.models import Sum

from inventory.models import *
from .models import *
from .forms import *

from django.db.models import Q

# Create your views here.

class ProviderView(LoginRequiredMixin, ListView):
    model = Provider
    context_object_name = 'obj'
    template_name = 'cmp/provider_list.html'
    
    def get_queryset(self): return Provider.objects.all()
    
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
    
    def get_queryset(self): return BuyHead.objects.all()
    

def buy(request, id_buy=None):
    template_name = 'cmp/buy.html'
    products = Product.objects.filter(user_created = request.user)
    form_buy = {}
    context = {}
    if request.method == "GET":
        form_buy = BuyForm()
        obj = BuyHead.objects.filter(Q(pk=id_buy) & Q(user_created = request.user)).first()
        
        if obj:
            details = BuyData.objects.filter(Q(buy=obj) & Q(user_created = request.user))
            date_buy = datetime.date.isoformat(obj.date_buy)
            date_fact = datetime.date.isoformat(obj.date_fact)
            e = {
                'id': obj.id,
                'date_buy': date_buy,
                'date_fact': date_fact,
                'provider': obj.provider,
                'observation': obj.observation,
                'no_fact': obj.no_fact,
                'sub_total': obj.sub_total,
                'offert': obj.offert,
                'total': obj.total,
            }
            
            form_buy = BuyForm(e)
        else: details = None
        
        context = {
            "products": products,
            "buy": obj,
            "details": details,
            "form_buy": form_buy,
        }
        
    if request.method=="POST":
        date_buy = request.POST.get('date_buy')
        observation = request.POST.get('observation')
        no_fact = request.POST.get('no_fact')
        date_fact = request.POST.get('date_fact')
        provider = request.POST.get('provider')
        sub_total = 0
        descuento = 0
        total = 0
        
        if not id_buy:
            prov = Provider.objects.get(pk=provider)
            head = BuyHead(
                date_buy = date_buy,
                observation = observation,
                no_fact = no_fact,
                date_fact = date_fact,
                provider = prov,
                user_created = request.user,
                user_modified = request.user,
            )
            if head:
                head.save()
                id_buy = head.id
        else:
            head = BuyHead.objects.get(pk=id_buy)
            if head:
                head.date_buy = date_buy
                head.observation = observation
                head.no_fact = no_fact
                head.date_fact = date_fact
                head.user_modified = request.user
                head.save()
        if not id_buy:
            return redirect('cmp:buy_list')
        
        product = request.POST.get('id_id_product')
        stock = request.POST.get('id_stock_details')
        price = request.POST.get('id_price_details')
        sub_total_details = request.POST.get('id_sub_total_details')
        offert_details = request.POST.get('id_offert_details')
        total_details = request.POST.get('id_total_details')
        
        prod = Product.objects.get(pk=product)
        
        det = BuyData(
            buy = head,
            product = prod,
            stock = stock,
            price = price,
            sub_total = sub_total_details,
            offert = offert_details,
            total = total_details,
            sell = 0,
            user_created = request.user,
            user_modified = request.user,
        )
        
        if det:
            det.save()
            sub_total = BuyData.objects.filter(Q(buy=id_buy) & Q(user_created = request.user)).aggregate(Sum('sub_total'))
            descuento = BuyData.objects.filter(Q(buy=id_buy) & Q(user_created = request.user)).aggregate(Sum('offert'))
            head.offert = descuento['offert__sum']
            head.sub_total = sub_total['sub_total__sum']        
            head.save()
            
        return redirect("cmp:buy_update", id_buy=id_buy)
            
    return render(request, template_name, context)
    