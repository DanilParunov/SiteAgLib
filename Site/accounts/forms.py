from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Customers, librarian
import datetime
from django.forms import ModelForm, TextInput, Textarea

class SignupUser(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='подтверждение пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    middle_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    number = forms.CharField(label='номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))
    residence = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields=('username','password1','password2', 'middle_name','number','residence')

    def save(self):
        user = super(SignupUser, self).save()
        customer = Customers(
            user = user,
            middle_name = self.cleaned_data['middle_name'],
            number=self.cleaned_data['number'],
            residence=self.cleaned_data['residence'],
            date = datetime.date(2012, 1, 1)
        )
        customer.save()
        return user

class SignupCustomer(UserCreationForm):
    middle_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Customers
        fields = ('middle_name',)
    number = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Customers
        fields = ('number',)

    residence = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Customers
        fields = ('residence',)



