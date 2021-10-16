import django_filters
from django_filters import DateFilter,CharFilter
from .models import *
from django import forms


class BillFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name="Bill_date",lookup_expr='gte')
    end_date = DateFilter(field_name="Bill_date", lookup_expr='lte')
    name=CharFilter(field_name="name", lookup_expr='icontains')


    class Meta:
        model=Bill
        fields='__all__'
        exclude=['sub_total','balance','last_updated','created_at','Bill_date']