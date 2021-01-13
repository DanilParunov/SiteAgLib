import include

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from list.models import Articles


class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField('Год рождения')
    middle_name = models.CharField(max_length=150, blank=True)
    number = models.CharField(max_length=150, blank=True)
    residence = models.CharField(max_length=150, blank=True)
    books = models.ManyToManyField(Articles)

    def __str__(self):
     return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural= 'Список Пользователей'

class librarian(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
     return self.title

    class Meta:
        verbose_name = 'Библиотекарь'
        verbose_name_plural= 'Список библиотекарей'

