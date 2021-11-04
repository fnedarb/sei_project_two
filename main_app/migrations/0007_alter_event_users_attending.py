# Generated by Django 3.2.8 on 2021-11-03 03:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0006_alter_event_users_attending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='users_attending',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
