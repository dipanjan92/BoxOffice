from django.shortcuts import render
from .models import Theatre, Show
import datetime

# Create your views here.


def theatre_list(request):
	theatres = Theatre.objects.all().order_by('city')
	theatre_list = []
	theatre_by_city = []
	city = theatres[0].city
	for i in range(0, len(theatres)):
		if city != theatres[i].city:
			city = theatres[i].city
			theatre_list.append(theatre_by_city)
			theatre_by_city = []
		theatre_by_city.append(theatres[i])

	theatre_list.append(theatre_by_city)

	return render(request, 'theatre/theatre_list.html', {'theatres': theatre_list})


def theatre_details(request, theatre_id):
	try:
		theatre_info = Theatre.objects.get(pk=theatre_id)
		shows = Show.objects.filter(theatre=theatre_id, 
			date=datetime.date.today()).order_by('movie')

		show_list = []
		show_by_movie = []
		movie = shows[0].movie
		for i in range(0, len(shows)):
			if movie != shows[i].movie:
				movie = shows[i].movie
				show_list.append(show_by_movie)
				show_by_movie = []
			show_by_movie.append(shows[i])

		show_list.append(show_by_movie)

		print(show_list)

	except Theatre.DoesNotExist:
		raise Http404("Page does not exist")
	return render(request, 'theatre/theatre_details.html', 
		{'theatre_info': theatre_info, 'show_list': show_list})
