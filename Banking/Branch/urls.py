from django.contrib import admin  
from django.urls import path  
from Branch import views  
urlpatterns = [    
    path('',views.show, name='show'),
    path('branch', views.branch),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  