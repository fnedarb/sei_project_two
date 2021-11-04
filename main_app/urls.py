from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profile/<int:pk>/edit/', views.ProfileUpdate.as_view(), name="profileupdate"),
    path('city/<int:pk>', views.CityDetailView.as_view(), name="city-detail"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('city/<int:pk>/post/new', views.PostCreate.as_view(), name="post-create"),
    path('post/<int:pk>/edit/', views.PostUpdate.as_view(), name="postupdate"),
    path('event/<int:pk>', views.EventDetailView.as_view(), name="event-detail"),
    path('event/<int:pk>/user/<int:user_pk>/', views.UserAttending.as_view(), name="user_attending"),
    path('city/', views.AllCities.as_view(), name="all-cities"),
    path('/post/<int:pk>/delete', views.DeletePost.as_view(), name='delete-post')
]