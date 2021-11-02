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
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
#@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["events"] = Event.objects.filter(
                name__icontains = name)
            context["cities"] = City.objects.filter(
                name__icontains = name)
        return context

#@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    model = Profile
    template_name='profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[]

class CityDetailView(TemplateView):
    model = City
    template_name='city_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.all()
        context["posts"] = Post.objects.all()
        return context

class EventDetailView(TemplateView):
    model = Event
    template_name='' # Add path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.all()
        return context



class PostCreate(CreateView):
    model = Post
    fields = ['title','date','image','content','upvotes']
    #template_name = ''

    def form_valid(self, form):
        form.instance.profile = self.request.profile # maybe user

    def get_success_url(self):
        return reverse('city_view', kwargs={'pk': self.object.pk})


class Signup(View):
    
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, " ", context) # Add path 
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, " ", context) # Add path