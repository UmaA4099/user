
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)


    def __str__(self):
        return self.username


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id']


class Dealer(models.Model):
    name = models.CharField(max_length=100, default=True)
    address = models.CharField(max_length=100, default=True)
    groups = models.ManyToManyField(Group, related_name='dealers')
    user_permissions = models.ManyToManyField(Permission, related_name='dealers')


    def __str__(self):
        return self.name
