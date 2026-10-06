from django.shortcuts import render
from .models import Post

def portfolio(request):
    return render(request, 'portfolio/index.html')


def blog(request):
    posts = Post.objects.all().order_by("-fecha")

    return render(request, "blog/index.html", {
        "posts": posts
    })