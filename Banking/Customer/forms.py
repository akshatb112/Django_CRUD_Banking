from django import forms  
from Customer.models import Customer

class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer  
        fields = "__all__" 

'''class AccountForm(forms.ModelForm):  
    class Meta:  
        model = Account  
        fields = "__all__" 
        '''