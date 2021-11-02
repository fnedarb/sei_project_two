from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import City, Profile, Event, Post
from django.db.models import Count, Q
from django.http import HttpResponse
from django import forms
from .forms import ProfileForm

# Create your views here.
class Home(TemplateView):
    template_name='home.html'

class ProfileView(TemplateView):
    template_name='profile.html'

class CityDetailView(TemplateView):
    template_name='city_view.html'


class Signup(View):
    def get(self, request):
        form = ProfileForm()
        context = {"form": form}
        return render (request, "registration/signup.html", context)

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.user.city = form.cleaned_data.get('city')
            user.user.age = form.cleaned_data.get('age')
            user.user.avatar = form.cleaned_data.get('avatar')
            user.save()
            login(request, user)
            return redirect ('profile')
        else:
            context = {"form": form}
            return render(request, 'registration/signup.html', context)