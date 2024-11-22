from django.shortcuts import render

from .models import Post, Categoria

# Create your views here.

def posts(request):
    contexto = {}
    posts = Post.objects.all().order_by("-id")
    contexto["posts"] = posts
    return render(request, 'blog/posts.html', contexto)