from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import BillForm,Bill_Detail_Form,BillSearchForm
from .models import Billinsert,Items,StudentData,Bill,Billing_Detail,Product
from django.db import connection
from django.contrib import messages
from .filters import BillFilter

# For Report Lab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
# End for report lab



import json

# Create your views here.
def home(request):
    # return HttpResponse("Jayalath_Enterprises")
    title="Jayalath Enterprises"
    header="Jayalath Enterprises Home Page"
    context={
        "title":title,
        "header":header,
    }
    return render(request,"index.html",context)

def add_invoice(request):
    title='Add Invoices'
    header='Add Invoices'
    products=Product.objects.all()
    # form=BillForm(request.POST or None)
    #
    # if form.is_valid():
    #     form.save()

    context={
        "title":title,
        "header":header,
        "products":products,


    }
    return render(request, 'addinvoice.html', context)




    # if request.method=="POST":
    #     if request.POST.get('Bill_number') and request.POST.get('Bill_date') and request.POST.get('name') and request.POST.get('sub_total') and request.POST.get('last_updated') and request.POST.get('paid') and request.POST.get('invoice_type') and request.POST.get('vehicle_number') and request.POST.get('product_name') and request.POST.get('price'):
    #         saverec=Billinsert()
    #         saverec.Bill_number=request.POST.get('Bill_number')
    #         saverec.Bill_date=request.POST.get('Bill_date')
    #         saverec.name=request.POST.get('name')
    #         saverec.sub_total=request.POST.get('sub_total')
    #         saverec.last_updated=request.POST.get('last_updated')
    #         saverec.paid=request.POST.get('paid')
    #         saverec.invoice_type=request.POST.get('invoice_type')
    #         saverec.vehicle_number =request.POST.get("vehicle_number")
    #         saverec.product_id_id=request.POST.get("product_name")
    #         saverec.total=request.POST.get("price")
    #
    #         cursor=connection.cursor()
    #         cursor.execute("call add_bills('"+saverec.Bill_number+"','"+saverec.Bill_date+"','"+saverec.name+"','"+saverec.sub_total+"','"+saverec.last_updated+"','"+saverec.paid+"','"+saverec.invoice_type+"','"+saverec.vehicle_number+"','"+saverec.product_id_id+"','"+saverec.total+"','"+100+"')")
    #         messages.success("The Bill saved")
    #
    #         return render(request,'addinvoice.html')
    # else:
    #     return render(request, 'addinvoice.html',context)

@csrf_exempt
def add_bills(request):
    title = "Jayalath Enterprises"
    header = "Jayalath Enterprises Home Page"
    context = {
        "title": title,
        "header": header
    }
    if request.method=="POST":


        item_name=request.POST.get('item_name')
        item_code=request.POST.get('item_code')
        item_desc=request.POST.get('item_desc')
        item_price=request.POST.get('price')

        saverec=Items()
        saverec.item_name=item_name
        saverec.item_code=item_code
        saverec.desc=item_desc
        saverec.price=item_price

        saverec.save()
        messages.info(request,'success')
        return render(request,"Addbills.html")

    else:
        messages.info(request,'fail')
    return render(request, "Addbills.html",context)

def homepage(request):
    title = "Jayalath Enterprises"
    header = "Jayalath Enterprises Home Page"
    students = StudentData.objects.all()
    context = {
        "title": title,
        "header": header,
        "students":students,
    }

    return render(request,'homepage.html', context)

@csrf_exempt
def InsertStudent(request):
    name=request.POST.get("name")
    email = request.POST.get("email")
    gender = request.POST.get("gender")

    try:
        student=StudentData(name=name,email=email,gender=gender)
        student.save()
        student_data={"id":student.id,"created_at":student.created_at,"error":False,"errorMessage":"Student added successfully"}
        return JsonResponse(student_data,safe=False)
    except:
        student_data={"error":True,"errorMessage":"Failed to add student"}
        return JsonResponse(student_data,safe=False)

@csrf_exempt
def update_all(request):
    data=request.POST.get("data")
    # print(data)
    dict_data=json.loads(data)
    # print(dict_data[0]['id'])

    try:
        for dic_single in dict_data:
            student=StudentData.objects.get(id=dic_single['id'])
            student.name=dic_single['name']
            student.email = dic_single['email']
            student.gender = dic_single['gender']
            student.save()

        student_data = {"error": False,"errorMessage": "Updated successfully"}
        return JsonResponse(student_data, safe=False)

    except:
        student_data = {"error": True, "errorMessage": "Failed to update"}
        return JsonResponse(student_data, safe=False)

@csrf_exempt
def delete_data(request):
    try:

        student=StudentData.objects.get(id=id)
        student.delete()

        student_data = {"error": False, "errorMessage": "Delete successfully"}
        return JsonResponse(student_data, safe=False)

    except:
        student_data = {"error": True, "errorMessage": "Failed to Delete"}
        return JsonResponse(student_data, safe=False)

@csrf_exempt
def save_all(request):
            data = request.POST.get("data")
            bill_number=request.POST.get("bill_number")
            bill_date=request.POST.get("bill_date")
            customer_name=request.POST.get("customer_name")
            type=request.POST.get("type")
            sub_total=request.POST.get("sub_total")


            print(bill_number)
            print(bill_date)
            print(customer_name)
            print(type)
            print(sub_total)

            print(data)

            dict_data=json.loads(data)

            bill = Bill()


            bill.Bill_number = bill_number
            bill.Bill_date = bill_date
            bill.name = customer_name
            bill.invoice_type = type
            bill.sub_total = sub_total

            bill.save()

            try:

                for data in dict_data:
                    vehicle_number= (data['vehicle_number'])
                    product_name= (data['product_name'])
                    price=(data['price'])

                    bill_details = Billing_Detail()
                    bill_details.vehicle_number=vehicle_number
                    bill_details.total=price
                    bill_details.Bill_number_id=bill_number
                    bill_details.product_id_id=product_name
                    bill_details.save()
            except:
                return render(request, 'addinvoice.html')


def list_of_invoices(request):
    title=''
    queryset=Bill.objects.all()
    form=BillSearchForm(request.GET or None)

    myFilter=BillFilter(request.GET,queryset=queryset)
    queryset=myFilter.qs

    context={
        "title":title,
        "queryset":queryset,
        "form": form,
        "myFilter":myFilter,

    }
    return render(request,"view_invoices.html",context)



