from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView): #CBV
    model = Post
    template_name = 'blog/index.html'
    ordering = '-pk'

"""
def index(request):  #FBV
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts
        }
    )
"""


def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )