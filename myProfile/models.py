from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Dodaj nowe pola, na przykład:
    GENDER_CHOICES = [
        ('f', 'Female'),
        ('m', 'Man'),
    ]
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
