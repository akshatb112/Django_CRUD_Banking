from django import forms  
from django.forms.widgets import NumberInput
from Customer.models import Customer

OCCUPATION_CHOICES = [
    ('Employed', 'Employed'),
    ('Business', 'Business'),
    ('Unemployed', 'Unemployed'),
    ('Student','Student')
]

class CustomerForm(forms.ModelForm):
    cmname=forms.CharField(required=False)
    occupation = forms.ChoiceField(choices=OCCUPATION_CHOICES)
    dateof_birth = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    address = forms.CharField(widget=forms.Textarea)  
    class Meta:  
        model = Customer  
        fields = "__all__" 

'''class AccountForm(forms.ModelForm):  
    class Meta:  
        model = Account  
        fields = "__all__" 
        '''