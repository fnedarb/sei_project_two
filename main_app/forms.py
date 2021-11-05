from django import forms
from django.db.models import aggregates, fields
from .models import Profile, Post, City, Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(UserCreationForm):
    age = forms.IntegerField(max_value=110)
    city = forms.ModelChoiceField(queryset=City.objects.all())
    avatar = forms.CharField(max_length=1000, label='Profile Picture', initial="https://media.istockphoto.com/vectors/woman-avatar-isolated-on-white-background-vector-illustration-for-vector-id1167753373?k=20&m=1167753373&s=612x612&w=0&h=88d0JshtPmZuJO3ybxNU9P-v-IHadT8PnPDNKdAFxCU=", help_text="Enter a profile image or leave the deault image, you can change this later.")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "city", "age", "avatar")

class ProfileUpdateForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all())
    avatar = forms.CharField(max_length=1000, label='Profile Picture')