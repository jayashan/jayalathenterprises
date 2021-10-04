from django.contrib import admin
from.models import Bill,Billing_Details,Products,Customer,Vehicle_Number

# Register your models here.

class Billing_Details_Admin(admin.ModelAdmin):
    list_display = ['id','Bill_number','product_id','qty','total']
    ordering = ['id']
    list_filter = ['Bill_number']
    search_fields = ['id']


class Bill_Admin(admin.ModelAdmin):
    list_display = ['Bill_number','name','sub_total']
    search_fields = ['Bill_number']



admin.site.register(Bill,Bill_Admin)
admin.site.register(Billing_Details,Billing_Details_Admin)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Vehicle_Number)