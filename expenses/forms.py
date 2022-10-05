from django import forms
from .models import Expense


class ExpenseSearchForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Expense
        fields = ('name', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['start_date'].required = False
        self.fields['end_date'].required = False
