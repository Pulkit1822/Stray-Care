from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email= models.EmailField(unique=True)
    first_name= models.CharField(max_length=30, blank=True)
    last_name= models.CharField(max_length=30, blank=True)
    date_of_birth= models.DateField(null=True, blank=True)
    bio= models.TextField(blank=True)

    def __str__(self):
        return self.username