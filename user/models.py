from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    review = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)