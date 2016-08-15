from django.shortcuts import render
from .models import Movie
from theatre.models import Show
import datetime

# Create your views here.


def movie_list(request):
	movies = Movie.objects.all().order_by('language')
	movie_list = []
	movie_by_lang = []
	lang = movies[0].language
	for i in range(0, len(movies)):
		if lang != movies[i].language:
			lang = movies[i].language
			movie_list.append(movie_by_lang)
			movie_by_lang = []
		movie_by_lang.append(movies[i])

	movie_list.append(movie_by_lang)

	return render(request, 'movie/movie_list.html', {'movies': movie_list})


def movie_details(request, movie_id):
	try:
		movie_info = Movie.objects.get(pk=movie_id)
		shows = Show.objects.filter(movie=movie_id, 
			date=datetime.date.today()).order_by('theatre')
		show_list = []
		show_by_theatre = []
		theatre = shows[0].theatre
		for i in range(0, len(shows)):
			if theatre != shows[i].theatre:
				theatre = shows[i].theatre
				show_list.append(show_by_theatre)
				show_by_theatre = []
			show_by_theatre.append(shows[i])

		show_list.append(show_by_theatre)

	except Movie.DoesNotExist:
		raise Http404("Page does not exist")
	return render(request, 'movie/movie_details.html', 
		{'movie_info': movie_info, 'show_list': show_list})
