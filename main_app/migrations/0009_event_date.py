# Generated by Django 3.2.8 on 2021-11-03 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_post_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
