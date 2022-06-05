from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from cmp.models import *

from inventory.models import *

from django.db.models import Sum

from todo.models import *

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'app/home.html'
    login_url = 'users:login'
    
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['productos'] = Product.objects.all().count()
        context['categorias'] = Category.objects.all().count()
        context['sub_categorias'] = SubCategory.objects.all().count()
        context['tareas'] = Task.objects.all().count()
        context['provedores'] = Provider.objects.all().count()
        return context