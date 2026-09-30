from django.shortcuts import render


def portfolio(request):
    return render(request, 'portfolio/index.html')


def blog(request):
    return render(request, 'blog/index.html')