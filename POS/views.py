import decimal
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, request, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import *
from .models import *
from django.db.models import F
from django.db import connection
from django.contrib import messages
from .filters import BillFilter,OrderFilter
from django.views.generic import ListView
import datetime
import random
from NEWS.models import Post
from django.db.models import Count
from datetime import date
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required




# For Report Lab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
# End for report lab

#------XHTML2PDF----------.
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
#--------END-------------.



import json
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    # return HttpResponse("Jayalath_Enterprises")
    title="Jayalath Enterprises"
    header="Jayalath Enterprises Home Page"
    product=Product.objects.all()
    fuel = Product.objects.all()
    traffic=Product.traffic
    news=Post.objects.all().order_by('-publish_date')
    news_category=Post.objects.values('category').annotate(dcount=Count('category')).order_by()
    latest=Post.objects.all().filter(publish_date=date.today())

    context={
        "title":title,
        "header":header,
        'product':product,
        'traffic':traffic,
        'fuel':fuel,
        'news':news,
        'news_category':news_category,
        'latest':latest

    }
    return render(request,"index.html",context)

def login(request):
    # login form method 2

    # title='login'
    #
    # if request.method=='POST':
    #     username=request.POST['username']
    #     password=request.POST['password']
    #
    #     user=auth.authenticate(username=username,password=password)
    #
    #     if user is not None:
    #         auth.login(request,user)
    #         return redirect('/settings_home')
    #     else:
    #         messages.info(request,'invalid credentials')
    #         return redirect('login')
    #
    # else:
    #     return render(request, 'login.html')

    # Login Form method 2
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                messages.info(request,f'Idiot..! you are logged in as {username}.')
                return redirect('/settings_home')
            else:
                messages.error(request,'Invalid username and password')
        else:
            messages.error(request,'Invalid username or password')

    form=AuthenticationForm()
    return render(request=request,template_name='login.html',context={'login_form':form})


def logout(request):
    auth.logout(request)
    return redirect('/')

def add_invoice(request):
    title='Add Invoices'
    header='Add Invoices'
    products=Product.objects.all()
    id=Product.product_id
    billnumber=random.randint(1, 10000000000)*2
    # stock=Stock.objects.filter(product='P92')
    # stock = Stock.objects.filter(product=id)

    stock=Stock.objects.all()
    invoice=Invoice.objects.all()


    # form=BillForm(request.POST or None)
    #
    # if form.is_valid():
    #     form.save()

    context={
        "title":title,
        "header":header,
        "products":products,
        "billnumber":billnumber,
        "stock":stock,


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
            stock=Stock.objects.all()

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
                    qty=(data['no_of_ltr'])
                    price=(data['price'])

                    bill_details = Billing_Detail()
                    bill_details.vehicle_number=vehicle_number
                    bill_details.total=price
                    bill_details.qty=qty
                    bill_details.Bill_number_id=bill_number
                    bill_details.product_id_id=product_name

                    bill_details.save()

                    if Stock.objects.filter(product=product_name):
                        Stock.objects.filter(product=product_name).update(qty=F('qty') - bill_details.qty)
                    else:
                        print('error')

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


def invoice_items(request,my_id):
    pk=my_id

    items=Bill.objects.get(Bill_number=my_id)

    vehicles=Billing_Detail.objects.filter(Bill_number=my_id)


    context={
        "pk":pk,
        "items":items,
        "vehicles":vehicles,
    }

    return render(request,"invoiceitems.html",context)


class CustomerListView(ListView):
    model = Bill
    template_name = 'main.html'

def customer_render_pdf_view(request,*args,**kwargs):
    pk=kwargs.get('pk')
    bill=get_object_or_404(Bill,pk=pk)
    items=Billing_Detail.objects.filter(Bill_number=pk)


    template_path = 'user_printer.html'
    context = {
        'customer': bill,
        'vehicles':items
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # if we want to download run this code
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # or if you just want to display in the browswe run this:
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdf_view(request):
    template_path = 'user_printer.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #if we want to download run this code
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    #or if you just want to display in the browswe run this:
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def settings_home(request):
    title='settings'
    orders = Order.objects.all()
    stock=Stock.objects.all()
    shift=Shift.objects.all()


    context={
        'title':title,
        'orders':orders,
        'stock':stock,
        'shift':shift,

    }
    return render(request,'settings_pages/index.html',context)


def Add_Fuels(request):
    title = 'Add_Fuels'
    queryset= Product.objects.all()
    form=Add_Fuels_Form(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,'Saved..!')
        return redirect('/Add_Fuels')

    context = {
        'title': title,
        'queryset':queryset,
        "form":form
    }
    return render(request,"settings_pages/Add_Fuels.html",context)


def Update_Fuels(request,pk):
    queryset=Product.objects.get(product_id=pk)

    form=Update_Fuels_Form(instance=queryset)

    if request.method=='POST':
        form=Update_Fuels_Form(request.POST,instance=queryset)

        if form.is_valid():
            form.save()
            return redirect('/Add_Fuels')

    context={
        'form':form
    }
    return render(request,"settings_pages/Add_Fuels.html",context)


def Delete_Fuels(request,pk):
    queryset=Product.objects.get(product_id=pk)
    if request.method=='POST':
        queryset.delete()
        return redirect('/Add_Fuels')

    return render(request,'settings_pages/Delete_Fuels.html')


def Add_Invoice(request):
    title='Add_Invoices'
    form=Add_Invoice_Form(request.POST or None)
    # queryset=Order.objects.all()
    orders=Order.objects.all()

    # myFilter=OrderFilter(request.GET,queryset=queryset)
    # queryset=myFilter.qs


    context={
        'title':title,
        'form':form,
        'order':orders,
        # 'queryset':queryset,
        # 'myFilter':myFilter
    }

    return render(request,'settings_pages/Add_Invoices.html',context)


def Make_Order(request):
    title='Orders'
    products=Product.objects.all()
    order=Order.objects.all()

    context={
        'title':title,
        'products':products,
    }
    return render(request,'settings_pages/Make_Order.html',context)


@csrf_exempt
def save_orders(request):
    today=datetime.datetime.now().strftime("%y%m%d")

    data=request.POST.get('data')
    order_number=request.POST.get('order_no')
    date=request.POST.get('date')
    name=request.POST.get('user')
    option = request.POST.get('option')


    key=today+'-'+order_number


    print(order_number)
    print(date)
    print(name)
    print(option)
    print(data)
    print(key)

    dict_data=json.loads(data)
    order=Order()

    order.order_no=key
    order.date_of_order=date
    order.made_by=name
    order.order_options=option

    order.save()

    try:
        for data in dict_data:
            product_name=(data['product_name'])
            qty=(data['qty'])

            order_items=Order_Item()

            order_items.order_no_id=key
            order_items.product_id=product_name
            order_items.qty=qty

            order_items.save()
    except:
        return render(request,'settings_pages/Make_Order.html')

    return render(request, 'settings_pages/Make_Order.html')


def view_order(request,*args,**kwargs):
    pk=kwargs.get('pk')


    order=get_object_or_404(Order,pk=pk)


    orders=Order.objects.get(pk=pk)
    items=orders.items.all()

    order_items=Order_Item.objects.all()
    products=Product.objects.all()



    context={
        'order':order,
        'items':items,

        'order_items':order_items,
        'products':products,



    }

    return render(request,'settings_pages/view_order.html',context)


def inventory(request):
    product=Product.objects.all()

    context={
        'product':product,
    }
    return render(request,'settings_pages/inventory.html',context)

@csrf_exempt
def save_invoices(request):
    OrderNo=request.POST.get('OrderNo')
    supplier=request.POST.get('supplier')
    InvoiceNo=request.POST.get('InvoiceNo')
    date=request.POST.get('date')
    VehicleNo=request.POST.get('VehicleNo')
    type=request.POST.get('type')
    TotalInvoice=request.POST.get('TotalInvoice')
    data=request.POST.get('data')

    print(OrderNo)
    print(InvoiceNo)
    print(date)
    print(VehicleNo)
    print(TotalInvoice)
    print(data)

    dict_data=json.loads(data)
    invoice=Invoice()

    invoice.invoice_number=InvoiceNo
    invoice.supplier_name = supplier
    invoice.order_number = OrderNo

    invoice.invoice_date=date
    invoice.invoice_total = TotalInvoice
    invoice.vehicle_number=VehicleNo
    invoice.invoice_type=type

    invoice.save()
    print(dict_data)

    try:

        for data in dict_data:
            ProductName=(data['ProductName'])
            Qty=(data['Qty'])
            rate=(data['rate'])
            ExtAmount=(data['ExtAmount'])
            Discount=(data['Discount'])
            NetAmount=(data['NetAmount'])

            items = Invoice_Item()

            items.invoice_number_id=InvoiceNo
            items.product_id = ProductName
            items.qty=Qty
            items.rate=rate
            items.extAmount=ExtAmount
            items.discount=Discount
            items.NetAmount=NetAmount

            items.save()

            print('success....!')

            if Stock.objects.filter(product=ProductName):
                Stock.objects.filter(product=ProductName).update(qty=F('qty') + items.qty)
            else:
                fuel_name = Product.objects.get(product_id=ProductName)


                s = Stock(product=fuel_name, qty=items.qty, type='FUEL', company_name='CPC', created_by='Anton')
                s.save()



    except:
        return render(request, 'settings_pages/inventory.html')
    return render(request,'settings_pages/inventory.html')


def shift_details(request,*args,**kwargs):
    pk = kwargs.get('id')
    s=Shift_Detail()
    shift = get_object_or_404(Shift, id=pk)
    price=0
    meter=0.00
    shift_money=Shift_Money.objects.filter(shift_id=shift.id)
    form=Shift_Money_Form(request.POST or None)
    shift_id=shift.id

    if request.method == 'POST' and 'btn_shift_money' in request.POST:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.shift_id = shift_id
            print(shift_id)
            form.save()
            messages.success(request, 'Saved..!')


    if request.method == 'POST' and 'btn_shift_details' in request.POST:
            shift_id = request.POST.get('id')
            shift_name = request.POST.get('shift_name')
            product=request.POST.get('product')
            pre_reading = request.POST.get('pre_reading')
            end_reading = request.POST.get('end_reading')

            used = request.POST.get('used')
            worker = request.POST.get('worker')
            operator_on = request.POST.get('operator_on')
            operator_off = request.POST.get('operator_off')
            profit=request.POST.get('profit')
            total=request.POST.get('total')



            print('shift id -'+shift_id)
            print('shift name -'+shift_name)
            print('product -'+product)
            print('pre reading -'+ pre_reading)
            print('end reading -'+str(end_reading))
            print('used -'+used)
            print('worker -'+worker)
            print('operator_on -'+operator_on)
            print('operator_off -'+operator_off)
            print('profit -'+profit)
            print('total -'+total)

            unit_price=Product.objects.filter(product_id=product).values_list('price',flat=True)
            Station.objects.filter(Station_Name=shift_name).update(meter=end_reading)
            Station.objects.filter(Station_Name=shift_name).update(Is_On=False)

            for n in unit_price:
                price = format(float(n)+100, '.2f')


            shift.EndReading=end_reading
            shift.Operator_ON=''
            shift.Operator_OFF=operator_off
            shift.Is_On=False

            s.Shift_ID_id = shift_id
            s.shift_Name = shift_name
            s.product_id=product
            s.PreReading = pre_reading
            s.EndReading =end_reading
            s.used=0.00
            s.worker = worker
            s.Operator_ON = operator_on
            s.Operator_OFF = operator_off
            s.Is_Using = False
            s.Profit=price

            print ('price' + price)
            shift.save()
            s.save()
            return redirect('/settings_home')

    context = {
        'shift': shift,
        'form': form,
        'shift_money':shift_money,
    }

    return render(request, 'settings_pages/shift_details.html', context)




def make_shifts(request):
    station=Station.objects.filter(Is_On=True)
    product=Product.objects.all()


    if request.method =='POST':
        shift_name=request.POST.get('Station_Name')
        product=request.POST.get('FuelCode')
        worker=request.POST.get('Pump_Operator')
        Pre_Reading=request.POST.get('meter')
        operator_on= request.POST.get('Operator_On')

        shift=Shift()
        shift.shift_Name_id=shift_name
        shift.product_id=product
        shift.worker=worker
        shift.PreReading=Pre_Reading
        shift.Operator_ON=operator_on
        Station.objects.filter(Station_Name=shift_name).update(Is_On=True)

        shift.save()
        messages.success(request,'saved')
        return redirect('/settings_home')

    context = {
        'station': station,
        'product':product,
    }

    return render(request,'settings_pages/make_shifts.html',context)


def Delete_Shift_Money(request,pk):
    queryset=Shift_Money.objects.get(pk=pk)
    queryset.delete()
    return redirect(request.META['HTTP_REFERER'])


def Add_Station(request):
    title='Add Stations'
    queryset=Station.objects.all()
    form=Station_Form(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,'Saved..!')
        return redirect('/Add_Station')

    context={
        'title':title,
        'form':form,
        'queryset':queryset,
    }
    return render(request,'settings_pages/Add_Station.html',context)
