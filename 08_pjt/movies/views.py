from django.shortcuts import render
from django.views.decorators.http import require_safe
from django.views.decorators.http import require_POST, require_http_methods
from .models import Movie, Genre
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render, redirect
import random
# Create your views here.
@require_http_methods(['GET', 'POST'])
@require_safe
def index(request):
    movies = get_list_or_404(Movie)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)



@require_safe
def recommended(request):
    movies = list(Movie.objects.all())
    random_movies = random.sample(movies, 10)
    context = {
        'random_movies': random_movies
    }
    return render(request, 'movies/recommended.html', context)