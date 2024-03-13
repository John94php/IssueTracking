from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    GENDER_CHOICES = [
        ('f', 'Female'),
        ('m', 'Male'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        db_table = "profile"


class Settings(models.Model):
    DARK_MODE = [
        ("1", "on"),
        ("0", "off")
    ]
    MAIL_NOTIFICATIONS = [
        ("1", "on"),
        ("0", "off")

    ]
    APP_NOTIFICATIONS = [
        ("1", "on"),
        ("0", "off")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dark_mode = models.CharField(max_length=1,choices=DARK_MODE)
    mail_notifications = models.CharField(max_length=1,choices=MAIL_NOTIFICATIONS)
    app_notifications = models.CharField(max_length=1, choices=APP_NOTIFICATIONS)

    class Meta:
        db_table = "settings"
