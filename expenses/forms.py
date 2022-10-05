from django import forms
from .models import Expense, Category


class ExpenseSearchForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    categories = forms.ModelMultipleChoiceField(label='Category', widget=forms.CheckboxSelectMultiple,
                                                queryset=Category.objects.all())

    class Meta:
        model = Expense
        fields = ('name', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['start_date'].required = False
        self.fields['end_date'].required = False
        self.fields['categories'].required = False
