from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	city = models.CharField(max_length=20)
	phone_regex = RegexValidator(regex=r'^[7-9]\d{9}$', message="Phone number must be of 10 digits")
	phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=10, null=True)

	def __str__(self):
		return self.user.username