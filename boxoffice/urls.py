from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('home.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^movie/', include('movie.urls')),
    url(r'^theatre/', include('theatre.urls')),
    url(r'^booking/', include('booking.urls')),
    url(r'^accounts/', include('user_profile.urls'))
]
