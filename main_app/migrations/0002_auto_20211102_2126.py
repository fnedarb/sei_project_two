# Generated by Django 3.2.8 on 2021-11-02 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='photo',
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.URLField(max_length=300, null=True),
        ),
    ]
