from django.urls import path, include
from  .views import Order_new


urlpatterns = [
    
    path('home/order', Order_new, name='order'),
    
   

]
