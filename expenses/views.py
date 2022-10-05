from django.views.generic.list import ListView

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category


class ExpenseListView(ListView):
    model = Expense
    data = Expense
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')


            if name:
                queryset = queryset.filter(name__icontains=name)

            if start_date:
                queryset = queryset.filter(date__gt=start_date)
            if end_date:
                queryset = queryset.filter(date__lt=end_date)




        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            **kwargs)

class CategoryListView(ListView):
    model = Category
    paginate_by = 5

