from django.shortcuts import render

from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView

from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin

from social.models import Post

from .forms import PostForm
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
    
def togglePost(request):
    id = request.GET.get('pk', None)
    try:
        obj = Post.objects.get(pk=id)
        if obj.state:
            obj.state = False
            obj.save()
        else:
            obj.state = True
            obj.save()
    except:
        print(request, "Ha ocurrido un error. Por favor intente de nuevo.")
    return reverse("social:feed")
