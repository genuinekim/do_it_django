# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostList(ListView): #CBV
    model = Post
    # template_name = 'blog/index.html'
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

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

class PostDetail(DetailView): #CBV
    model = Post
    # template_name = 'blog/single_post_page.html'

"""
def single_post_page(request, pk): # FBV
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )
"""