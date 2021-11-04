from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profile/<int:pk>/edit/', views.ProfileUpdate.as_view(), name="profileupdate"),
    path('city/<int:pk>', views.CityDetailView.as_view(), name="city-detail"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('city/<int:pk>/post/new', views.PostCreate.as_view(), name="post-create"),
    path('event/<int:pk>', views.EventDetailView.as_view(), name="event-detail"),
]