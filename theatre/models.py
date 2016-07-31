from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie

# Create your models here.

class Theatre(models.Model):
    city_choice=(
        ('DELHI','Delhi'),
        ('KOLKATA','Kolkata'),
        ('MUMBAI','Mumbai'),
        ('CHENNAI','Chennai'),
        ('BANGALORE','Bangalore'),
        ('HYDERABAD','Hyderabad'),
    )
    name = models.CharField(max_length=50,null=False)
    city = models.CharField(max_length=9,choices=city_choice,null=False)
    address = models.CharField(max_length=30)
    no_of_screen = models.IntegerField()
    admin_id = models.ForeignKey(User)

    def __str__(self):
        return self.name+"-"+self.address+"-"+self.city

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screen = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.movie) + "-" + str(self.theatre) + "-" + str(self.date) + "-" + str(self.time)