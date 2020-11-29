from account.models import Product
from django.shortcuts import render


def home(request):
    return render(request, 'account/dashboard.html')


def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'account/products.html', context)


def customers(request):
    return render(request, 'account/customers.html')
