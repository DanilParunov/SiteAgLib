from django.urls import path, include
from.import views
urlpatterns = [
    path('', views.index, name='home'),
    path('o', views.o, name='about'),
    path('Acc', views.Account, name='Account')

]