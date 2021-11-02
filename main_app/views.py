from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import City, Profile, Event, Post
from django.db.models import Count, Q
from django.http import HttpResponse

# Create your views here.
class Home(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.all()
        context["cities"] = City.objects.all()
        return context

class ProfileView(TemplateView):
    template_name='profile.html'

class CityDetailView(TemplateView):
    template_name='city_view.html'
