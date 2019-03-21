from django.shortcuts import render
from django.http import HttpResponse
from . import populate_db as pdb


def index(request):
    return render(request, 'rw_main/index.html')
