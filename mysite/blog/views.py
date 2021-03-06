from django.shortcuts import render,HttpResponse
from django.views import generic
from .models import Post

def fun(request):
    return render(request,'pg.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

# Create your views here.
