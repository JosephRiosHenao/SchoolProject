from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'app/home.html'
    login_url = 'users:login'