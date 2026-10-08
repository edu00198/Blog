from django.shortcuts import render, get_object_or_404
from .models import Post, Comentario


def blog(request):
    posts = Post.objects.all().order_by('-fecha')

    return render(request, 'blog/index.html', {
        'posts': posts
    })


def detalle_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        contenido = request.POST.get("contenido")

        if nombre and contenido:
            Comentario.objects.create(
                post=post,
                nombre=nombre,
                contenido=contenido
            )

    comentarios = post.comentarios.all().order_by("-fecha")

    return render(request, "blog/detalle.html", {
        "post": post,
        "comentarios": comentarios
    })