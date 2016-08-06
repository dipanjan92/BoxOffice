from django.shortcuts import render
from movie.models import Movie

# Create your views here.


def show_index(request):
	movie_list = Movie.objects.all()

	return render(request, 'common/home.html', {'movie_list': movie_list})
