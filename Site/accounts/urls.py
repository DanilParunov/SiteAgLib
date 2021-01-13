from django.urls import path, include
from.import views
from .views import SignUpView, register, Profile


urlpatterns = [
    path('signup/', register, name='signup'),
    path('Profile/', views.Profile, name='profile'),

]