from django import forms  
from Branch.models import Branch

class BranchForm(forms.ModelForm):  
    class Meta:  
        model = Branch  
        fields = "__all__"  

'''class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer  
        fields = "__all__" 

class AccountForm(forms.ModelForm):  
    class Meta:  
        model = Account  
        fields = "__all__" 
        '''