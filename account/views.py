from django.shortcuts import render


def home(request):
    return render(request, 'account/dashboard.html')


def products(request):
    return render(request, 'account/products.html')


def customers(request):
    return render(request, 'account/customers.html')
