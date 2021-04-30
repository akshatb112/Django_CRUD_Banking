from django.db import models  
class Branch(models.Model):    
    bname = models.CharField(max_length=100)  
    bcity = models.CharField(max_length=20)    
    class Meta:  
        db_table = "branch" 

'''class Customer(models.Model):    
    cfname = models.CharField(max_length=50)
    cmname = models.CharField(max_length=50, null=True)
    clname = models.CharField(max_length=50)  
    mobile_no = models.CharField(max_length=10)
    occupation = models.CharField(max_length=30)
    dateof_birth = models.DateField()
    class Meta:  
        db_table = "customer"   

class Account(models.Model):    
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bid = models.ForeignKey(Branch, on_delete=models.CASCADE)
    open_balance = models.IntegerField()
    open_date = models.DateField()
    account_type = models.CharField(max_length=10)  
    account_status = models.CharField(max_length=10)
    class Meta:  
        db_table = "account" 



'''