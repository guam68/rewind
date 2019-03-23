from django.urls import path
from . import views


app_name = 'rw_main'

urlpatterns = [
        path('', views.index, name='index'),
        path('browse', views.browse, name='browse'),
        path('search', views.search, name='search'),
        path('get_random', views.get_random_movies, name='get_random_movies'),
        path('detail', views.get_movie_details, name='get_movie_details'),
]