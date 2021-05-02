from django.db import models
from Customer.models import Customer
from Branch.models import Branch 
from django.contrib.postgres.fields import ArrayField 
from django.utils import timezone
   

class BankAccount(models.Model):    
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bid = models.ForeignKey(Branch, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    open_date = models.DateField()
    account_type = models.CharField(max_length=20)  
    cards = ArrayField(
        models.CharField(max_length=20),
        size=2,
    )

    class Meta:  
        db_table = "bankaccount" 