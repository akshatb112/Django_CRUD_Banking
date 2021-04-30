from django.contrib import admin  
from django.urls import path  
from Customer import views  
urlpatterns = [    
    path('',views.index, name='index'),
    path('cus', views.cus),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  