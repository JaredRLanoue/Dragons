from django.db import models
from django.contrib.auth.models import AbstractUser


#Custom user model using Django's AbstractUser model, parameters subject to change
class User(AbstractUser):
    firstName = models.CharField(max_length=30, blank=True)
    lastName = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    groups = models.ManyToManyField('auth.Group', blank=True, related_name="user_set")

