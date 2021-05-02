from django.contrib import admin  
from django.urls import path  
from Customer import views
from django.conf.urls.static import static
from django.conf import settings
from Branch import views as b_views
from BankAccount import views as a_views

urlpatterns = [    
    path('',views.show, name='show'),
    path('cus', views.cus),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('branc', b_views.branc),
    path('branch_show',b_views.branch_show),
    path('b_edit/<int:id>', b_views.edit),  
    path('b_update/<int:id>', b_views.update),  
    path('b_delete/<int:id>', b_views.destroy),
    path('acc', a_views.acc),  
    path('account_show',a_views.account_show),  
    path('a_edit/<int:id>', a_views.edit),  
    path('a_update/<int:id>', a_views.update),  
    path('a_delete/<int:id>', a_views.destroy),  

]  

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)