from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)

# Custom group model using Django again, including the user model created above as the user type field
class Groups(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    visibility = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="groups_created",
    )
    admins = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="groups_administered"
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="groups_joined"
    )

    def __str__(self):
        return self.title
