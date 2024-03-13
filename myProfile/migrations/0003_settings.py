# Generated by Django 5.0.2 on 2024-03-13 09:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProfile', '0002_alter_profile_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dark_mode', models.CharField(choices=[('1', 'on'), ('0', 'off')], max_length=1)),
                ('mail_notifications', models.CharField(choices=[('1', 'on'), ('0', 'off')], max_length=1)),
                ('app_notifications', models.CharField(choices=[('1', 'on'), ('0', 'off')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'settings',
            },
        ),
    ]
