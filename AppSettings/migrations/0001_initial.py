# Generated by Django 5.0.2 on 2024-03-16 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "app_name",
                    models.CharField(default="Issue Tracking", max_length=100),
                ),
                ("app_timezone", models.CharField(default="UTC", max_length=100)),
                ("logo", models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]