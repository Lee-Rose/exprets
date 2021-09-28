from django.shortcuts import render
from .models import Article

def week(request):
    news = Article.objects.all().order_by('title')
    return render(request, '../../main/films.html', news)

def film_detail(request, slug):
    detail = Article.objects.get(slug=slug)
    return render(request, 'films/films_detail.html', {'detail':detail})
