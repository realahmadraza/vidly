from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

def detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)
