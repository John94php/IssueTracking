from django.db import models


# Create your models here.

class Settings(models.Model):
    app_name = models.CharField(max_length=100, default="Issue Tracking")
    app_timezone = models.CharField(max_length=100,default="UTC")
    logo = models.CharField(max_length=255,blank=True)
    class Meta:
        db_table = "app_settings"

