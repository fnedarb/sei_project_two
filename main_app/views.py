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
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
#@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["events"] = Event.objects.all()
        context["cities"] = City.objects.all()
        context["profile"] = Profile.objects.filter(user=self.request.user)
        return context

#@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name='profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.filter(users_attending__id=self.request.user.id)
        context["post"] = Post.objects.filter(id=self.request.user.id)
        context["profile"] = Profile.objects.filter(user=self.request.user)
        return context

class CityDetailView(TemplateView):
    model = City
    template_name='city_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.filter(city=self.object.pk)
        context["posts"] = Post.objects.filter(city=self.objects.pk)
        return context

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


class EventDetailView(TemplateView):
    model = Event
    template_name='' # Add path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.filter(city=self.object.pk)
        return context



class PostCreate(CreateView):
    model = Post
    fields = ['title','date','image','content','upvotes']
    #template_name = ''

    def form_valid(self, form):
        form.instance.profile = self.request.profile # maybe user

    def get_success_url(self):
        return reverse('city_view', kwargs={'pk': self.object.pk})

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'photo', 'content']
    template_name = " "
    success_url = "/profile/"

class PostDelete(DeleteView):
    model = Post
    template_name = " "
    success_url = "/profile/"


