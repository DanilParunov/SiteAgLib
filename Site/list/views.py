from django.shortcuts import render, redirect
from .models import Articles
from accounts.models import Customers
from .models import Library, CustomersBooks
from .forms import ArticlesForm
from django.views.generic import DetailView



class LibDetail(DetailView):
    model = Library
    template_name = 'list/lib_detail.html'
    context_object_name = 'lib'


class BookDetail(DetailView):
    model = Articles
    template_name = 'list/detail.html'
    context_object_name = 'book'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = Customers.objects.get(user_id=self.request.user.id)
        context['books'] = context['customer'].books.all()
        return context

def list_index(request):
    # list = Articles.objects.all()
    list = Articles.objects.order_by('title')  # сортировка по алфавиту (минус (-) перед полем которе сортируется - сортировка в обратную сторону)
    return render(request, 'list/list_index.html', {'list':list})



def library_list_index(request):
    # list = Articles.objects.all()
    lib_list = Library.objects.order_by('title')  # сортировка по алфавиту (минус (-) перед полем которе сортируется - сортировка в обратную сторону)
    return render(request, 'list/library_list_index.html', {'lib_list':lib_list})

def create(request):
    error = ''
    if request.method =='POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_home')
        else:
            error = 'Неверное заполнение полей'

    form = ArticlesForm()
    data = {

        'form': form,
        'error':error
    }

    return render(request, 'list/create.html',data)

def add_book(request, pk):
    customer = Customers.objects.get(user_id=request.user.id)
    l = CustomersBooks(customer=customer, article=Articles.objects.get(pk=pk))
    l.save()
    # customer.save()
    # customer.books.add(Articles.objects.get(pk=pk))
    return redirect('home')

def remove_book(request, book_pk, customer_pk):
    c_book = Articles.objects.get(pk=book_pk)
    customer = Customers.objects.get(pk=customer_pk)
    books = CustomersBooks.objects.get(article=c_book, customer=customer)
    books.delete()
    return redirect('home')