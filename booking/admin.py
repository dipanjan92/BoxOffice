from django.contrib import admin
from .models import Booking, Seat, BookedSeat

# Register your models here.

admin.site.register(Booking)

admin.site.register(Seat)

admin.site.register(BookedSeat)