from django.db import models

# Create your models here.

class Bill(models.Model):
    Bill_number=models.IntegerField(primary_key=True )
    Bill_date=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    name=models.CharField('Customer Name',max_length=120,default='',blank=True,null=True)

    sub_total=models.IntegerField()
    balance=models.IntegerField(default='0', blank=True,null=True)
    last_updated=models.DateField(auto_now_add=False,auto_now=True,blank=True)
    paid=models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True,null=False)
    invoice_type_choice=(
        ('Paid','Paid'),
        ('Cash','Cash'),
        ('Debit','Debit'),
    )
    invoice_type=models.CharField(max_length=100,default='',blank=True,null=True,choices=invoice_type_choice)

    def __str__(self):
        return self.Bill_number

class Product(models.Model):
    product_id=models.CharField(primary_key=True,max_length=50)
    product_name=models.CharField(max_length=100)
    price=models.IntegerField('Unit Price',default=0,blank=True,null=True)
    order_level=models.IntegerField('Pre Order Level', default=0,blank=True,null=True)

    def __str__(self):
        return self.product_name


class Billing_Detail(models.Model):
    id=models.BigAutoField(primary_key=True)
    Bill_number=models.ForeignKey(Bill,null=True,on_delete=models.SET_NULL)
    product_id=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    vehicle_number=models.CharField(max_length=50)
    qty=models.IntegerField(null=True,default=0)
    total=models.IntegerField()


    def __str__(self):
        return self.Bill_number


class Customer(models.Model):
    company_id=models.IntegerField(null=False)
    company_name=models.CharField(max_length=100)


    def __str__(self):
        return self.company_name

class Vehicle_Number(models.Model):
    company_id=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    vehicle_number=models.CharField(max_length=100)

    def __str__(self):
        return self.vehicle_number


class Billinsert(models.Model):
    Bill_number=models.IntegerField()
    Bill_date=models.DateField()
    name=models.CharField(max_length=100)
    sub_total=models.IntegerField()
    last_updated=models.DateField()
    paid=models.BooleanField()
    invoice_type=models.CharField(max_length=100)
    vehicle_number=models.CharField(max_length=100)
    qty=models.IntegerField()
    total=models.IntegerField()
    product_id_id=models.CharField(max_length=100)

class Items(models.Model):
    item_name=models.CharField(max_length=50)
    item_code=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    price=models.IntegerField()


class Details(models.Model):
    id=models.AutoField(primary_key=True)
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    City=models.CharField(max_length=30)


class StudentData(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=225)
    gender=models.CharField(max_length=225)
    created_at=models.DateField(auto_now_add=True)
    objects=models.Manager()


class Bills(models.Model):
    id=models.BigAutoField(primary_key=True)
    vehicle_number=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    price=models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    objects = models.Manager()
