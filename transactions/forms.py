from django import forms
from .models import Transaction
import sweetify
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount',]

    



