from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    product_id=models.CharField(primary_key=True,max_length=50)
    product_name=models.CharField(max_length=100)
    price=models.DecimalField('Unit Price',max_digits=10,decimal_places=2,default=0.00)
    evaporation=models.DecimalField('Evaporation Allowance', max_digits=10, decimal_places=2, default=0.00)
    brought_price=models.DecimalField('Brought Price',max_digits=10,decimal_places=2,default=0.00)
    discount=models.DecimalField(max_digits=10,decimal_places=2,null=False,default=0.00)
    availability=models.IntegerField(null=False,default=0)
    traffic=models.IntegerField(null=False,default=0)
    arrival_date=models.CharField(max_length=100,null=True,blank=True,default='')


    BADGES_TYPE_CHOICES=[
        ('primary','primary'),
        ('secondary','secondary'),
        ('danger','danger'),
        ('warning','warning'),

    ]

    CATEGORY_TYPE_CHOICES=[
        ('GOODS','Goods'),
        ('FUEL','Fuel'),
    ]
    category_type=models.CharField(max_length=50,default='',blank=False,null=False,choices=CATEGORY_TYPE_CHOICES)
    css_color_code = models.CharField(max_length=100,default='',blank=True,choices=BADGES_TYPE_CHOICES)

class Supplier(models.Model):
    supplier_id=models.BigAutoField(primary_key=True)
    supplier_name=models.CharField(max_length=50, null=False,blank=False)
    supplier_address1=models.CharField(max_length=50, null=True,blank=True)
    supplier_address2 = models.CharField(max_length=50, null=True, blank=True)
    city=models.CharField(max_length=50, null=True, blank=True)

    PHONE_NUMBER_CHOICES=[
        ('LAND1','LAND1'),
        ('LAND2', 'LAND2'),
        ('MOBILE','MOBILE')
    ]

    phone_number=models.CharField(max_length=50,default='',blank=True,null=True,choices=PHONE_NUMBER_CHOICES)


class Stock(models.Model):
    stock_id=models.BigAutoField(primary_key=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='stock_products')
    qty=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

    TYPE_CHOICES=[
        ('FUEL','FUEL'),
        ('GOODS','GOODS')
    ]
    type=models.CharField(max_length=50,blank=False,null=False,choices=TYPE_CHOICES)
    company_name=models.CharField(max_length=100,blank=False,null=False)
    created_by=models.CharField(max_length=100,blank=False,null=False)
    pre_order_level=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    update_date=models.DateTimeField(auto_now_add=True,null=False)


class Order(models.Model):
    order_no=models.CharField(primary_key=True,null=False,blank=False,max_length=50)
    date_of_order=models.DateField(auto_now_add=False,auto_now=False,blank=False)
    made_by=models.CharField(max_length=100,null=False,blank=False)
    created_on=models.DateTimeField(auto_now=True,null=False)
    ORDER_OPTIONS_CHOICES=[
        ('TP','Telephone'),
        ('Post','POST'),
        ('fax','Fax'),

    ]
    order_options=models.CharField(max_length=50,null=False,choices=ORDER_OPTIONS_CHOICES)
    Is_pending=models.BooleanField(default=True)

    def __str__(self):
        return str(self.order_no)

class Order_Item(models.Model):
    order_item_no=models.BigAutoField(primary_key=True)
    order_no=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='products',on_delete=models.DO_NOTHING, null=False, blank=False)
    qty = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    Is_received = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True, null=False)


    def __str__(self):
        return str(self.order_no) + '-' +str(self.order_item_no)


class Invoice(models.Model):
    invoice_number=models.BigIntegerField(primary_key=True,null=False,blank=False)
    supplier_name=models.CharField(max_length=50)
    order_number=models.CharField(null=False,blank=False,max_length=50)
    invoice_date = models.DateField(auto_now_add=False, auto_now=False, blank=False, null=False)
    invoice_total=models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False)
    vehicle_number=models.CharField(max_length=100,null=False,blank=False)
    INVOICE_TYPE_CHOICES=[
        ('CASH','CASH'),
        ('CREDIT','CREDIT'),
    ]

    invoice_type=models.CharField(max_length=50,null=True,choices=INVOICE_TYPE_CHOICES)
    created_on=models.DateTimeField(auto_now=True,null=False)
    is_received=models.BooleanField(default=True)

    def __str__(self):
        return str(self.invoice_number) + '-' + str(self.order_number)


class Invoice_Item(models.Model):
    id=models.BigAutoField(primary_key=True)
    invoice_number=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    qty=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    extAmount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    NetAmount=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

    def __str__(self):
        return str(self.invoice_number)



class Bill(models.Model):
    Bill_number=models.BigIntegerField(primary_key=True)
    Bill_date=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    name=models.CharField('Customer Name',max_length=120,default='',blank=True,null=True)

    sub_total=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    balance=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    last_updated=models.DateField(auto_now_add=False,auto_now=True,blank=True)
    paid=models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True,null=False)
    invoice_type_choice=(
        ('Paid','Paid'),
        ('Cash','Cash'),
        ('Debit','Debit'),
    )
    invoice_type=models.CharField(max_length=100,default='',blank=True,null=True,choices=invoice_type_choice)

class Billing_Detail(models.Model):
    id=models.BigAutoField(primary_key=True)
    Bill_number=models.ForeignKey(Bill,null=True,on_delete=models.SET_NULL)
    product_id=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    vehicle_number=models.CharField(max_length=50)
    qty=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    total=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)


class Station(models.Model):
    Station_Name=models.CharField(primary_key=True,max_length=50,null=False)
    Station_Fuel=models.ForeignKey(Product,on_delete=models.DO_NOTHING,related_name='station_fuel')
    Is_On=models.BooleanField(default=False)
    meter = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Station_Date = models.DateTimeField(auto_now=True, null=False)



    def __str__(self):
        return str(self.Station_Name)


class Shift(models.Model):
    id = models.BigAutoField(primary_key=True)
    shift_Name = models.ForeignKey(Station, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True,related_name='shift_product')
    worker = models.CharField(max_length=50, null=True, blank=True)
    PreReading = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    EndReading = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Operator_ON = models.CharField(max_length=50, null=True, blank=True)
    Operator_OFF = models.CharField(max_length=50, null=True, blank=True)
    Is_On = models.BooleanField(default=True)

    def __str__(self):
        return str(self.shift_Name)


class Shift_Detail(models.Model):
    id = models.BigAutoField(primary_key=True)
    Shift_ID=models.ForeignKey(Shift,related_name='shift',on_delete=models.CASCADE)
    shift_Name=models.CharField(max_length=50,null=False,blank=True)
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING,null=True,blank=True)
    PreReading=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    EndReading=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    used=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    worker=models.CharField(max_length=50)
    Operator_ON=models.CharField(max_length=50,null=False)
    Operator_OFF=models.CharField(max_length=50,null=True,blank=True)
    Shift_On_Date=models.DateTimeField(auto_now=True, null=False)
    Shift_Off_Date=models.DateTimeField(auto_now=True, null=False)
    Is_Using=models.BooleanField(default=True)
    Pre_Money=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    Profit=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    Total=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    Short_money=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)


    def __str__(self):
        return str(self.Shift_ID)


class Shift_Money(models.Model):
    id=models.BigAutoField(primary_key=True)
    shift=models.ForeignKey(Shift,on_delete=models.CASCADE,default=0)
    amount=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    date=models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return str(self.id) +'-'+str(self.shift)


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



