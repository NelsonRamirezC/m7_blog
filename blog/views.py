from django.shortcuts import render

from .models import Post, Categoria, Comentario

from django.contrib.auth.decorators import login_required, permission_required

from django.contrib import messages
from django.shortcuts import redirect

from .forms import PostFormCreate

# Create your views here.

def posts(request):
    contexto = {}
    posts = Post.objects.all().order_by("-id")
    contexto["posts"] = posts
    return render(request, 'blog/posts.html', contexto)

def detalle_post(request, post_id):
    contexto = {}
    try:
        post = Post.objects.get(id=post_id)
        
        comentarios = Comentario.objects.all().filter(post=post)
        
        
    except post.DoesNotExist as e:
        messages.error(request, f"No existe un post con el id: {post_id}")
        return redirect('posts')
    
        
    
    contexto["post"] = post
    contexto["comentarios"] = comentarios
    return render(request, 'blog/detalle_post.html', contexto)


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
            # print(model_post.autor.id)
            model_post.save()
            
            messages.success(request, "Post creado con éxito.")
            return redirect('posts')
            
        else:
            messages.error(request, "Algo ha fallado, revise bien los datos ingresados.")
            return render(request, 'blog/crear_post.html', contexto)


def agregar_comentario(request, post_id):
    if request.method == "POST":
        contenido = request.POST.get("contenido")
        
        post = Post.objects.get(id=post_id)
        
        print(contenido)
        print(post)
        print(request.user)
        
        nuevo_comentario = Comentario(contenido=contenido, post=post, autor=request.user)
        
        nuevo_comentario.save()

        messages.success(request, "Comentario creado con éxito")
        return redirect('detalle_post', post_id)
    else:
        messages.error(request, "Acción / método no permitido")
        return redirect('posts')