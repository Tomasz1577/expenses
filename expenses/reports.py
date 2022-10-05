from collections import OrderedDict

from django.db.models import Sum, Value
from django.db.models.functions import Coalesce, TruncMonth


def summary_per_category(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))

#4.add total amount spent.
#5.add table with total summary per year-month.

def get_per_year_month_summary(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(year_month=TruncMonth('date'),)
        .order_by()
        .values('year_month')
        .annotate(sum=Sum('amount'))
        .values_list('year_month','sum')
    ))

def total_amount(queryset):
    return OrderedDict(
        queryset.aggregate(Sum('amount'))
    )