from . import views
from django.urls import path


urlpatterns = [
    path('', views.week, name='films_home'),
    path('<slug:slug>/', views.film_detail, name='detail')
]
