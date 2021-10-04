from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import BillForm,Bill_Details_Form
from .models import Billinsert,Items,StudentData,Bills,Billing_Details
from django.db import connection
from django.contrib import messages
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
    form=BillForm(request.POST or None)


    if form.is_valid():
        form.save()

    context={
        "title":title,
        "header":header,
        "form":form,

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
    data=request.POST.get("data")
    print(data)
    dict_data=json.loads(data)

    for data in dict_data:
        bill_number=(data['bill_number'])
        vehicle_number= (data['vehicle_number'])
        product_name= (data['product_name'])
        price=(data['price'])


        # bill=Bills()
        # bill.vehicle_number=vehicle_number
        # bill.product_name=product_name
        # bill.price=price

        bill=Billing_Details()

        bill.vehicle_number=vehicle_number
        bill.total=price
        bill.Bill_number_id='1234'
        bill.product_id_id='3'

        bill.save()





    return render(request, 'addinvoice.html')














