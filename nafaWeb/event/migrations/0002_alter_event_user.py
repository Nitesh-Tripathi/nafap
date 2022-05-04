# Generated by Django 4.0.4 on 2022-05-04 06:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='members_in_event', to=settings.AUTH_USER_MODEL),
        ),
    ]
