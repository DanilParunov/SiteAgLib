from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupUser, SignupCustomer
from django.urls import reverse_lazy
from django.views import generic
from .models import Customers
from list.models import Articles, CustomersBooks
from django.views.generic import DetailView, TemplateView

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

def register(request):
    if request.method=='POST':
        user_form = SignupUser(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('home')
    else:
        user_form = SignupUser()
    return render(request, 'accounts/signup.html',{'user_form':user_form})

def Profile(request):
    customer = Customers.objects.get(user_id=request.user.id)
    return render(request, 'accounts/Profile.html', {
        'customer': customer,
        'customers': Customers.objects.all(),
        'customer_books': customer.books.all(),
        'books': Articles.objects.all(),
        'all_books': CustomersBooks.objects.all()
    })

# class Profile(LoginRequiredMixin, TemplateView):
#     model = Customers
#     template_name = 'accounts/Profile.html'
#     context_object_name = 'customer'
#     login_url = ''
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

