from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('city/<int:pk>', views.CityDetailView.as_view(), name="city-detail"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]