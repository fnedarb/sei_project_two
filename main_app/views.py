from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import City, Profile, Event, Post
from django.db.models import Count, Q, Sum
from django.http import HttpResponse
from django import forms
from .forms import ProfileForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
#@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search")
        context["events"] = Event.objects.all().annotate(count=Count('users_attending__user')).order_by('-count')[:3]
        context["cities"] = City.objects.all()[:3]
        if (self.request.user.is_authenticated):
            context["currentprofile"] = Profile.objects.filter(user=self.request.user)
        return context

#@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model = Profile
    template_name='profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.filter(users_attending__user=self.object.user)
        context["posts"] = Post.objects.filter(profile=self.object.user).order_by('-date')
        if (self.request.user.is_authenticated):
            context["currentprofile"] = Profile.objects.filter(user=self.request.user)
        return context

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['city', 'avatar']
    template_name = "profileupdate.html"

    def get_success_url(self):
        pk = Profile.objects.get(user=self.request.user)
        return reverse('profile', args=[str(pk.id)])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if (self.request.user.is_authenticated):
            context["currentprofile"] = Profile.objects.filter(user=self.request.user)
        return context

class CityDetailView(DetailView):
    model = City
    template_name='city_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(city=self.object.pk).order_by('-date')
        if (self.request.user.is_authenticated):
            context["currentprofile"] = Profile.objects.filter(user=self.request.user)
        return context


class EventDetailView(DetailView):
    model = Event
    template_name='event_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profiles"] = Profile.objects.all()
        if (self.request.user.is_authenticated):
            context["currentprofile"] = Profile.objects.filter(user=self.request.user)
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
            return redirect ('home')
        else:
            context = {"form": form}
            return render(request, 'registration/signup.html', context)



class PostCreate(View):
    def post(self, request, pk):
        profile = self.request.user
        title = request.POST.get('postTitle')
        city = City.objects.get(pk=pk)
        content = request.POST.get('postContent')
        upvotes = 0
        photo = request.POST.get('postImage')
        Post.objects.create(profile=profile, title=title, city=city, content=content, upvotes=upvotes, photo=photo)
        return redirect('city-detail', pk=pk)

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'photo', 'content']
    template_name = "post_update.html"
    
    def get_success_url(self):
        pk = Profile.objects.get(user=self.request.user)
        return reverse('profile', args=[str(pk.id)])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if (self.request.user.is_authenticated) and (self.request.user):
            context["currentprofile"] = Profile.objects.filter(user=self.request.user)
        return context



class UserAttending(View):
    def get(self, request, pk, user_pk):
        user_pk = Profile.objects.get(user=self.request.user.pk)
        print(user_pk)
        attending = request.GET.get("attending")
        if (attending == "remove"):
            Event.objects.get(pk=pk).users_attending.remove(user_pk)
        if (attending == "add"):
            Event.objects.get(pk=pk).users_attending.add(user_pk)
        return redirect('event-detail', pk=pk)



class AllCities(TemplateView):
    template_name='all_cities.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search")
        if (search != None):
            context["cities"] = City.objects.filter(Q(name__icontains=search)|Q(state__icontains=search)|Q(country__icontains=search))
            context["header"] = f"Search for '{search}'"
        else:
            context["cities"] = City.objects.all()
            context["header"] = "All Cities"
        if (self.request.user.is_authenticated):
            context["currentprofile"] = Profile.objects.filter(user=self.request.user)
        return context


class DeletePost(DeleteView):
    model = Post
    template_name = "profile.html"

    def get_success_url(self):
        pk = Profile.objects.get(user=self.request.user)
        return reverse('profile', args=[str(pk.id)])


class AllEvents(TemplateView):
    template_name='all-events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search")
        if (search != None):
            context["events"] = Event.objects.filter(Q(name__icontains=search))
            context["header"] = f"Search for '{search}'"
        else:
            context["cities"] = City.objects.all()
            context["events"] = Event.objects.all()
            context["header"] = "All Cities"
        if (self.request.user.is_authenticated):
            context["currentprofile"] = Profile.objects.filter(user=self.request.user)
        return context