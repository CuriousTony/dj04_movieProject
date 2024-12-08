from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Movie
from .forms import MovieForm


def home(request):
    movies = Movie.objects.all().order_by('name')
    return render(request, 'movie_app/home.html', {'movies': movies})


def upload(request):
    error = ''
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
        else:
            error = 'Данные карточки заполнены некорректно'
    else:
        form = MovieForm()
        return render(request, 'movie_app/upload.html', {'form': form, 'error': error})


def about(request):
    return render(request, 'movie_app/about.html')
