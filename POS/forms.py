from django import forms
from.models import Bill,Billing_Detail,Product,Invoice
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
        fields=['product_id','product_name','price','Evap_amount','brought_price','discount','category_type']


class Update_Fuels_Form(forms.ModelForm):
    class Meta:
        model=Product
        fields = ['product_id', 'product_name', 'price','Evap_amount','brought_price','discount','category_type']


class Add_Invoice_Form(forms.ModelForm):
    class Meta:
        model=Invoice
        fields=['invoice_number','invoice_date','invoice_total','vehicle_number','invoice_type','order_number']

