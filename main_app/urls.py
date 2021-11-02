from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('city/', views.CityDetailView.as_view(), name="city-detail"),
<<<<<<< HEAD
    # path('account/signup/', views.Signup.as_view(), name="singup")
=======
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
>>>>>>> 65b8bcbc41441f0775da270a10871e40875ac834
]