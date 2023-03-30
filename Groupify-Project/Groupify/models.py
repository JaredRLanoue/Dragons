from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import get_user_model

#Custom user model using Django's AbstractUser model, parameters subject to change
class User(AbstractUser):
    firstName = models.CharField(max_length=30, blank=True)
    lastName = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    groups = models.ManyToManyField('auth.Group', blank=True, related_name="user_set")

User = get_user_model()

#Custom group model using Django again, including the user model created above as the user type field
class Group(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    visibility = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='groups_created')
    admins = models.ManyToManyField(User, related_name='groups_administered')
    users = models.ManyToManyField(User, related_name='groups_joined')

    def __str__(self):
        return self.title