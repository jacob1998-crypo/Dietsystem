from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.first_name