from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def week(request):
    return render(request, 'main/films.html')

def watchlist(request):
    return render(request, 'main/watchlist.html')

def sign_in(request):
    return render(request, 'main/sign_in.html')


