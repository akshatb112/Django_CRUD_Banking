from django.contrib import admin  
from django.urls import path  
from Branch import views  

urlpatterns = [    
    path('',views.branch_show, name='branch_show'),
    path('branc', views.branc, name='branch_add'),  
    path('branch_show',views.branch_show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),

]  