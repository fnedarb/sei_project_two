from django.contrib import admin
from .models import City, Profile, Event, Post

# Register your models here.
admin.site.register(City)
admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Post)