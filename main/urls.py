from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('films_list', views.week, name='films_list'),
    path('watchlist', views.watchlist, name='watchlist'),
    path('sign_in', views.sign_in, name='sign_in'),
]
