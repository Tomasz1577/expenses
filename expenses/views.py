from django.views.generic.list import ListView

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category, get_per_year_month_summary, total_amount


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            #1.allow searching by date (from and/or to).
            #2.allow searching by multiple categories.
            #3.add sorting by category or date (ascending and descending)
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            categories = form.cleaned_data['categories']
            sort_date = form.cleaned_data['sort_date']
            sort_category = form.cleaned_data['sort_category']


            if name:
                queryset = queryset.filter(name__icontains=name)
            if start_date:
                queryset = queryset.filter(date__gt=start_date)
            if end_date:
                queryset = queryset.filter(date__lt=end_date)
            if categories:
                categories_list = [Category.objects.get(name=category) for category in categories]
                queryset = Expense.objects.filter(category__in=categories_list)
            if sort_date == 'ascending':
                queryset = queryset.order_by('date')
            elif sort_date == 'descending':
                queryset = queryset.order_by('-date')
            if sort_category == 'ascending':
                queryset = queryset.order_by('category')
            elif sort_category == 'descending':
                queryset = queryset.order_by('-category')





        return super().get_context_data(
            # 4.add total amount spent.
            # 5.add table with total summary per year-month.
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            get_per_year_month_summary= get_per_year_month_summary(queryset),
            amount=total_amount(queryset),
                **kwargs)

class CategoryListView(ListView):
    model = Category
    paginate_by = 5

