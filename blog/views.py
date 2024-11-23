from django.shortcuts import render

from .models import Post, Categoria

from django.contrib.auth.decorators import login_required, permission_required

from django.contrib import messages
from django.shortcuts import redirect

from .forms import PostFormCreate

# Create your views here.

def posts(request, post_id):
    contexto = {}
    posts = Post.objects.all().order_by("-id")
    contexto["posts"] = posts
    return render(request, 'blog/posts.html', contexto)


@login_required(login_url="login")
@permission_required("blog.add_post", login_url="index")
def crear_post(request):
    contexto = {}
    contexto["form"] = PostFormCreate()
        
    if request.method == 'GET':
        return render(request, 'blog/crear_post.html', contexto)
    
    if request.method == 'POST':
        
        form = PostFormCreate(request.POST)
        contexto["form"] = form 
        
        if form.is_valid():
            model_post = form.instance
            
            model_post.autor = request.user
            print(model_post.autor.id)
            model_post.save()
            
            messages.success(request, "Post creado con éxito.")
            return redirect('posts')
            
        else:
            messages.error(request, "Algo ha fallado, revise bien los datos ingresados.")
            return render(request, 'blog/crear_post.html', contexto)
