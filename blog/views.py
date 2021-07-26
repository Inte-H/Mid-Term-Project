from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class Index(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/index.html'


class Post(DetailView):
    model = Post
    template_name = 'blog/post.html'

# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts,
#         }
#     )

# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post' : post
#         }
#     )