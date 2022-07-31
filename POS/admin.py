from django.contrib import admin
from.models import *

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
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(Order_Item)
admin.site.register(Invoice)
admin.site.register(Invoice_Item)
admin.site.register(Supplier)
admin.site.register(Station)
admin.site.register(Shift)
admin.site.register(Shift_Detail)
admin.site.register(Shift_Money)
admin.site.register(Post)
admin.site.register(Category)







