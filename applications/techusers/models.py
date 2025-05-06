from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.


class TechUser(AbstractUser):
    email = models.EmailField(max_length=100, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_of_birth = models.DateField(null=False, default=datetime.date(2005, 1, 1))

    def __str__(self):
        return self.username
