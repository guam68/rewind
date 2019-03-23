from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import json
from .models import Movie


def index(request):
    return render(request, 'rw_main/index.html')


def browse(request):
    return render(request, 'rw_main/browse.html')


def search(request):
    return HttpResponse("ar")


def get_random_movies(request):
    movies = Movie.objects.order_by('?')[:10]

    movie_json = {}
    for i, movie in enumerate(movies):
        movie_json[i] = model_to_dict(movie)
    return JsonResponse(movie_json)


def get_movie_details(request):
    data = json.loads(request.body)
    details = Movie.objects.get(id=data['id'])
    details = model_to_dict(details)
    return JsonResponse(details)