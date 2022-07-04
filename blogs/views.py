from django.shortcuts import render
from .models import BlogModel
from django.views.generic import ListView, DetailView



class BlogsView(ListView):
    model = BlogModel
    template_name = 'main/posts.html'
    paginate_by = 1
    page_kwarg = 'blog'

class BlogsDetailView(DetailView):
    mode = BlogModel
    template_name = 'main/blog_in.html'