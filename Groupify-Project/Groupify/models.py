from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

#Custom user model using Django's AbstractUser model, parameters subject to change
#Firstname and Lastname already exist within AbstractUser, so no need to define them here
class User(AbstractUser):
    email = models.EmailField()
    groups = models.ManyToManyField(Group, blank=True, related_name="group_members")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='groupify_user_permissions')

    def __str__(self):
        return self.email


# Custom group model using Django again, including the user model created above as the user type field
class Group(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    visibility = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='groups_created')
    admins = models.ManyToManyField(User, related_name='groups_administered')
    members = models.ManyToManyField(User, related_name='groups_joined')

    def __str__(self):
        return self.title
