from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')
def o(request):
    return render(request, 'main/o.html')
def Account(request):
    return render(request, 'main/Account.html')

