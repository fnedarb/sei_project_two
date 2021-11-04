from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic import dates

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    country = models.CharField(max_length = 200)
    image = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name="user")
    city = ForeignKey(City, on_delete = models.CASCADE, related_name = "city", null=True)
    age = models.IntegerField(default=18, null=True)
    avatar = models.URLField(max_length = 600, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.user.save()



class Event(models.Model):
    name = models.CharField(max_length = 1000)
    city = models.ForeignKey(City, on_delete = models.CASCADE, related_name = "event_city")
    venue = models.CharField(max_length = 200)
    description = models.TextField(max_length = 5000)
    address = models.TextField(max_length = 2000)
    users_attending = models.ManyToManyField(Profile, null=True)
    image = models.URLField(max_length = 300, null=True)
    date=models.DateField(null=True)

    def __str__(self):
        return self.name



class Post(models.Model):
    profile = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 1000)
    city = models.ForeignKey(City, on_delete = models.CASCADE, related_name = "post_city")
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length = 5000)
    upvotes = models.IntegerField(default=0)
    photo = models.URLField(max_length = 300)

    def __str__(self):
        return self.title













