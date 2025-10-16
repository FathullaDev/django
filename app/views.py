from django.shortcuts import render
from app.models import *

def index(request):
    shippers = Shippers.objects.all()
    orders = Orders.objects.all()
    employees = Employees.objects.all()
    customers = Customers.objects.all()
    products = Products.objects.all()
    suppliers = Suppliers.objects.all()
    categories = Categories.objects.all()


def orders(request):
    orders = Orders.objects.all()
    content={
        "orders": orders
    }
    return render(request,'orders.html',content)


def employees(request):
    employees = Employees.objects.all()
    content={
        "employees": employees
    }
    return render(request,'employees.html',content)

def customers(request):
    customers = Customers.objects.all()
    content={
        "customers": customers
    }
    return render(request,'customers.html',content)

def products(request):
    products = Products.objects.all()
    content={
        "products": products
    }
    return render(request,'products.html',content)

def suppliers(request):
    suppliers = Suppliers.objects.all()
    content={
        "suppliers": suppliers
    }
    return render(request,'suppliers.html',content)


def categories(request):
    categories = Categories.objects.all()
    content={
        "categories": categories
    }
    return render(request,'categories.html',content)

def shippers(request):
    shippers = Shippers.objects.all()
    content={
        "shippers": shippers
    }
    return render(request,'shippers.html',content)
