from django.contrib import admin  
from django.urls import path  
from BankAccount import views

urlpatterns = [    
    path('',views.account_show, name='account_show'),
    path('acc', views.acc),  
    path('account_show',views.account_show),  
    path('a_edit/<int:id>', views.edit),  
    path('a_update/<int:id>', views.update),  
    path('a_delete/<int:id>', views.destroy),
]  

