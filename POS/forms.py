from django import forms
from.models import Bill,Billing_Details
import datetime

class BillForm(forms.ModelForm):
    class Meta:
        model=Bill
        fields=['Bill_number','Bill_date','name',
                'sub_total','invoice_type'

        ]
class Bill_Details_Form(forms.ModelForm):
    class Meta:
        model=Billing_Details
        fields=['vehicle_number'

        ]


