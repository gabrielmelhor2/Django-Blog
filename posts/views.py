from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import *
from django.db.models import Q

def posts_view(request):
    query = request.GET.get('search', None)  # 'search' é o nome do campo de busca
    
    if query and len(query) > 1:  # Certifique-se de que a busca tem mais de 1 caractere
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        if query:  # Se a busca for inválida (menor que 2 caracteres ou só espaço), retorna nenhum post
            posts = Post.objects.none()
        else:  # Se o usuário não digitou nada, mostra todos os posts
            posts = Post.objects.all()

    return render(request, "posts.html", {'posts': posts})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o post no banco de dados
            return redirect(('posts_view'))  # Redireciona após o post ser salvo
    else:
        form = PostForm()

    return render(request, 'new_post.html', {'form': form})
    
    