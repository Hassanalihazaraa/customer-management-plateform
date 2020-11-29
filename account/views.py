from account.models import Customer, Order, Product
from django.shortcuts import render


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    context = {
        'orders': orders,
        'customers': customers,
    }
    return render(request, 'account/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'account/products.html', context)


def customers(request):
    return render(request, 'account/customers.html')
