from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect

from django.shortcuts import render

from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, RedirectView, View

from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin

from social.models import Post

from .forms import PostForm

from django.http import JsonResponse


# Create your views here.

class CreatePost(LoginRequiredMixin, CreateView):
    template_name = 'social/create_post.html'
    form_class = PostForm
    success_url = reverse_lazy('social:feed')
    
class ListsPosts(ListView):
    template_name = 'social/list_feed.html'
    model = Post
    ordering = '-created'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):        
        return super().get_context_data(**kwargs)
    
    
class DetailPost(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'social/detail_post.html'
    queryset = Post.objects.all()
    context_object_name = 'post'
    
# class tooglePost(LoginRequiredMixin, View):
#     template_name = "base.html"
    
#     def get(self, *args, **kwargs):
#         pk = self.kwargs.get('pk')
#         post = Post.objects.get(id=pk)
#         post.state = False if post.state else True
#         post.save()
#         print("Estado cambiado con exito a {}".format(post.state))
        
def togglePost(request):
    id = request.GET.get('pk', None)
    try:
        obj = Post.objects.get(id=id)
        obj.state = False if obj.state else True
        obj.save()
        print("Se logró activar/desactivar.")
        return JsonResponse({'success': True})
    except:
        print("No se logró activar/desactivar.")
        return JsonResponse({'pk': 0})