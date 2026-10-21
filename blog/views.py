from django.shortcuts import render, get_object_or_404
from .models import MAX_COMENTARIO_LENGTH, Post, Comentario


def blog(request):
    posts = Post.objects.all().order_by('-fecha')

    return render(request, 'blog/index.html', {
        'posts': posts
    })


def detalle_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    error_comentario = None

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        contenido = request.POST.get("contenido")

        if nombre and contenido:
            if len(contenido) > MAX_COMENTARIO_LENGTH:
                error_comentario = (
                    f"El comentario no puede superar los "
                    f"{MAX_COMENTARIO_LENGTH} caracteres."
                )
            else:
                Comentario.objects.create(
                    post=post,
                    nombre=nombre,
                    contenido=contenido
                )

    comentarios = post.comentarios.all().order_by("-fecha")

    return render(request, "blog/detalle.html", {
        "post": post,
        "comentarios": comentarios,
        "error_comentario": error_comentario,
        "max_comentario_length": MAX_COMENTARIO_LENGTH,
    })