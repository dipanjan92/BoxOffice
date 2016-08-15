from django.shortcuts import render
from movie.models import Movie

# Create your views here.


def show_index(request):
	movie_list = Movie.objects.all().order_by('popularity_index')
	top_movie = Movie.objects.all().order_by('popularity_index')[:3]

	return render(request, 'common/home.html', {'movie_list': movie_list, 
		'top_movie': top_movie})
