from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.movie_list, name='movie_list'),
	url(r'^(?P<movie_id>\d+)/$', views.movie_details, name='movie_details')	
]