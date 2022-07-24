from django import forms
from django.forms import modelform_factory, HiddenInput

from .models import *
import datetime

class BillForm(forms.ModelForm):
    class Meta:
        model=Bill
        fields=['Bill_number','Bill_date','name',
                'sub_total','invoice_type'

        ]
class Bill_Detail_Form(forms.ModelForm):
    class Meta:
        model=Billing_Detail
        fields=['vehicle_number'

        ]

class BillSearchForm(forms.ModelForm):
    generate_invoice = forms.BooleanField(required=False)
    class Meta:
        model=Bill
        fields=['generate_invoice']


class Add_Fuels_Form(forms.ModelForm):
    class Meta:
        model=Product
        fields=['product_id','product_name','price','evaporation','brought_price','discount','category_type']


class Update_Fuels_Form(forms.ModelForm):
    class Meta:
        model=Product
        fields = ['product_id', 'product_name', 'price','evaporation','brought_price','discount','category_type']


class Add_Invoice_Form(forms.ModelForm):
    class Meta:
        model=Invoice
        fields=['invoice_number','invoice_date','invoice_total','vehicle_number','invoice_type','order_number']


class Make_Shifts_Form(forms.ModelForm):
    class Meta:
        model=Shift
        fields=['shift_Name','product','worker','PreReading','Operator_ON']

class Shift_Money_Form(forms.ModelForm):
    class Meta:
        model=Shift_Money
        fields=['id','shift','amount']

class Station_Form(forms.ModelForm):
    class Meta:
        model=Station
        fields=['Station_Name','Station_Fuel','meter']


