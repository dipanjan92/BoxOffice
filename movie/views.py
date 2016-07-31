from django.shortcuts import render
from .models import Movie
from theatre.models import Show
import datetime

# Create your views here.


def movie_list(request):
	movies = Movie.objects.all()
	return render(request, 'movie/movie_list.html', {'movies': movies})


def movie_details(request, movie_id):
	try:
		movie_info = Movie.objects.get(pk=movie_id)
		show_list = Show.objects.filter(movie=movie_id, 
			date=datetime.date.today())
	except Movie.DoesNotExist:
		raise Http404("Page does not exist")
	return render(request, 'movie/movie_details.html', 
		{'movie_info': movie_info, 'show_list': show_list})
