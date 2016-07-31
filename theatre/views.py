from django.shortcuts import render
from .models import Theatre, Show
import datetime

# Create your views here.


def theatre_list(request):
	theatres = Theatre.objects.all()
	return render(request, 'theatre/theatre_list.html', {'theatres': theatres})


def theatre_details(request, theatre_id):
	try:
		theatre_info = Theatre.objects.get(pk=theatre_id)
		show_list = Show.objects.filter(theatre=theatre_id, 
			date=datetime.date.today())
	except Theatre.DoesNotExist:
		raise Http404("Page does not exist")
	return render(request, 'theatre/theatre_details.html', 
		{'theatre_info': theatre_info, 'show_list': show_list})
