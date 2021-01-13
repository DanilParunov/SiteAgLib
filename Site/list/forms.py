from .models import Articles
from .models import Library
from django.forms import ModelForm, TextInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'date']

        widgets = {

            "title":TextInput(attrs={
                  'class': 'form-control',
                  'placeholder': 'Название книги'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            }),

            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
            "date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
        }
class LibraryForm(ModelForm):
    class Meta:
        model = Library
        fields = ['title', 'addres', 'text', ]

        widgets = {

            "title":TextInput(attrs={
                  'class': 'form-control',
                  'placeholder': 'Название книги'
            }),
            "addres": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),

            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
        }

