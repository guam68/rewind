from . import credentials as cred
import requests
import json
from time import sleep

from .models import Movie

# poster img sample url
# https://image.tmdb.org/t/p/w185_and_h278_bestv2/yE5d3BUhE8hCnkMUJOo1QDoOGNz.jpg


site = ('http://api.themoviedb.org/3/discover/movie?primary_release_date.gte=1985-09-15&primary_release_date.lte=2007-10-22?&api_key=',
        '&page=')


def get_movies(site, page):
    response = requests.get(site[0] + cred.api_key + site[1] + str(page)).json()
    results = response['results']
    movie_objs = []

    for result in results:
        new_movie = Movie(
                id = result['id'],
                title = result['title'],
                overview = result['overview'],
                poster_img = result['poster_path'],
                genre_id = ','.join([str(num) for num in result['genre_ids']]),
                release_date = result['release_date']
            )
        movie_objs += [new_movie]

    Movie.objects.bulk_create(movie_objs, ignore_conflicts=True)
    sleep(2)  


        

# for i in range(2,200):
#     get_movies(site, i)
#     print(i)