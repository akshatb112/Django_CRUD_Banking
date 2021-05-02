from django.db import models  

class Customer(models.Model):    
    cfname = models.CharField(max_length=50)
    cmname = models.CharField(max_length=50, null=True)
    clname = models.CharField(max_length=50)  
    mobileno = models.CharField(max_length=10)
    occupation = models.CharField(max_length=30, null=True)
    dateof_birth = models.DateField()
    address = models.CharField(max_length=150)
    Image = models.ImageField(null=True,blank=True,upload_to='images')
    Signature = models.ImageField(null=True,blank=True,upload_to='signatures')
    class Meta:  
        db_table = "customer"   

'''class Account(models.Model):    
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bid = models.ForeignKey(Branch, on_delete=models.CASCADE)
    open_balance = models.IntegerField()
    open_date = models.DateField()
    account_type = models.CharField(max_length=10)  
    account_status = models.CharField(max_length=10)
    class Meta:  
        db_table = "account" 



'''
