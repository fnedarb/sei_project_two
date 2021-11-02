from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name='home.html'

class ProfileView(TemplateView):
    template_name='profile.html'

class CityDetailView(TemplateView):
    template_name='city_view.html'