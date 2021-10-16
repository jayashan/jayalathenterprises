from django.contrib import admin
from.models import Bill,Billing_Detail,Product,Customer,Vehicle_Number

# Register your models here.

class Billing_Detail_Admin(admin.ModelAdmin):
    list_display = ['id','Bill_number','product_id','qty','total']
    ordering = ['id']
    list_filter = ['Bill_number']
    search_fields = ['id']


class Bill_Admin(admin.ModelAdmin):
    list_display = ['Bill_number','name','sub_total']
    search_fields = ['Bill_number']



admin.site.register(Bill,Bill_Admin)
admin.site.register(Billing_Detail,Billing_Detail_Admin)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Vehicle_Number)
