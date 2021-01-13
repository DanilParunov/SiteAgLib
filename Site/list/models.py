from django.db import models
from django.urls import reverse


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Автор', max_length=250)
    text = models.TextField('Текст')
    date = models.DateField('Дата выпуска')

    def __str__(self):
     return self.title

    def get_absolute_url(self):
        return reverse('book', {'book_id': self.pk})

    class Meta:
        verbose_name = 'Список литературы'
        verbose_name_plural = 'Список литературы'

class CustomersBooks(models.Model):
    customer = models.ForeignKey(to='accounts.Customers', on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)


class Library(models.Model):
    title = models.CharField('Название', max_length=50)
    addres = models.CharField('Адрес',max_length=250)
    text = models.TextField('Текст')


    def __str__(self):
     return self.title

    class Meta:
        verbose_name = 'Список Библиотек'
        verbose_name_plural= 'Список библиотек'
