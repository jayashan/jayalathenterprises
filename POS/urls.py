"""jayalathenterprises URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from.import views
# from .views import News_Home_Page,NewsDetailView,AddNewsView,UpdateNewsView,DeleteNewsView
from NEWS.views import NewsDetailView


urlpatterns = [
    path("",views.home,name='home'),
    path("add_bills/",views.add_bills,name='add_bills'),
    path('add_invoice/',views.add_invoice,name='add_invoice'),
    path('save_all/',views.save_all,name='save_all'),

    path('list_invoices/',views.list_of_invoices,name='list_invoices'),


    path('homepage/',views.homepage,name='homepage'),
    path('insert_student/',views.InsertStudent,name='insert'),
    path('delete_data',views.delete_data,name='delete_data'),
    path('update_all/',views.update_all,name='update_all'),

    path('invoice_items/<pk>/',views.invoice_items,name='invoice_items'),



    path('print/',views.render_pdf_view,name='print-pdf-testing'),
    path('print2/',views.CustomerListView.as_view(),name='print-list-view'),

    path('pdf/<pk>/',views.customer_render_pdf_view,name='print-customer-view'),


    # settings pages

    path('settings_home/',views.settings_home,name='settings_home'),
    path('Add_Fuels/',views.Add_Fuels,name='Add_Fuels'),
    path('Update_Fuels/<str:pk>/',views.Update_Fuels,name='Update_Fuels'),
    path('Delete_Fuels/<str:pk>/',views.Delete_Fuels,name='Delete_Fuels'),


    path('make_shifts/',views.make_shifts,name='make_shifts'),




    path('test/',views.Add_Invoice,name='Add_Invoice'),


    path('Make_Order/',views.Make_Order,name='Make_Order'),
    path('save_orders/',views.save_orders,name='save_orders'),
    path('view_order/<pk>/',views.view_order,name='view_order'),



    path('inventory/',views.inventory,name='inventory'),
    path('save_invoices/',views.save_invoices,name='save_invoices'),


    path('shift_details/<str:id>/',views.shift_details,name='shift_details'),
    # path('shift_off',views.Shift_Off,name='shift_off'),
    path('Delete_Shift_Money/<str:pk>',views.Delete_Shift_Money,name='Delete_Shift_Money'),


    path('Add_Station/',views.Add_Station,name='Add_Station'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    #==========NEWS======================

    path('post/<int:pk>',NewsDetailView.as_view(),name='post-detail'),


]
