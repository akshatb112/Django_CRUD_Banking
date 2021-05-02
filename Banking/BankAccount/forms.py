from django import forms  
from BankAccount.models import BankAccount
from django.forms.widgets import NumberInput

ACCOUNT_TYPE_CHOICES = [
    ('Current', 'Current'),
    ('Savings', 'Savings'),
]

CARD_CHOICES = [
    ('Credit', 'Credit Card'),
    ('Debit', 'Debit Card'),
]

class BankAccountForm(forms.ModelForm):
    cname = BankAccount.cid
    balance = forms.FloatField()
    open_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    account_type = forms.ChoiceField(widget=forms.RadioSelect, choices=ACCOUNT_TYPE_CHOICES)
    cards = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=CARD_CHOICES) 
    class Meta:  
        model = BankAccount  
        fields = "__all__" 