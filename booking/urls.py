from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^seatchoice/(?P<show_id>\d+)/$', views.reserve_seat, name='reserve_seat'),
	url(r'^payment/$', views.payment_gateway, name='payment_gateway'),
	url(r'^payment_confirmation/$', views.payment_confirmation, name='payment_confirmation')
]