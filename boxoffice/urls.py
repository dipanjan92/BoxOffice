from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^$', include('home.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^movie/', include('movie.urls')),
    url(r'^theatre/', include('theatre.urls')),
    url(r'^booking/', include('booking.urls')),
    url(r'^accounts/', include('user_profile.urls'))
]

if settings.DEBUG:
	urlpatterns += patterns('django.views.static', (r'^media/(?P<path>.*)', 
		'serve', {'document_root': settings.MEDIA_ROOT}), )
