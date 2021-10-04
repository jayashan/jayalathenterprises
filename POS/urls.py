"""JayalathEnterprises URL Configuration

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

urlpatterns = [
    path("",views.home,name='home'),
    path("add_bills/",views.add_bills,name='add_bills'),
    path('add_invoice/',views.add_invoice,name='add_invoice'),
    path('save_all/',views.save_all,name='save_all'),

    path('homepage/',views.homepage,name='homepage'),
    path('insert_student/',views.InsertStudent,name='insert'),
    path('delete_data',views.delete_data,name='delete_data'),
    path('update_all/',views.update_all,name='update_all'),







]
