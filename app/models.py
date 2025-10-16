from django.db import models
from django.db.models import CharField, ForeignKey, AutoField
from django.db.models.fields import return_None


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category_name

class Suppliers(models.Model):
    supplier_id=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Products(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100)
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    supplier = models.ForeignKey(Suppliers,on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.product_name


class Customers(models.Model):
    customer_id=models.AutoField(primary_key=True)
    company_name=CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Employees(models.Model):
    employee_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer=models.ForeignKey(Customers, on_delete=models.CASCADE,default=1)
    employee=models.ForeignKey(Employees, on_delete=models.CASCADE, default=1)
    order_date=models.DateField()
    ship_name=models.CharField(max_length=100)

    def __str__(self):
        return self.ship_name


class Shippers(models.Model):
    shipper_id=AutoField(primary_key=1)
    company_name=CharField(max_length=100)

    def __str__(self):
        return self.company_name



