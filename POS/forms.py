from django import forms
from.models import Bill,Billing_Detail
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


