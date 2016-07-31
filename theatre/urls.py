from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.theatre_list, name='theatre_list'),
	url(r'^(?P<theatre_id>\d+)/$', views.theatre_details, name='theatre_details')	
]