# Generated by Django 3.2.8 on 2021-11-04 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_merge_20211103_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='users_attending',
            field=models.ManyToManyField(null=True, to='main_app.Profile'),
        ),
    ]