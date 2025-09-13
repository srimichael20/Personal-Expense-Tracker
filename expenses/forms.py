from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category']
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Amount'}),
            'category': forms.TextInput(attrs={'placeholder': 'Category'}),
        }
