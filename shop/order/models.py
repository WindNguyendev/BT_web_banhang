from django.db import models
from cart.models import Cart
from django.contrib.auth.models import User


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default="", null=False)
    phone = models.CharField(max_length=10,default="",null=False)
    shiping_address = models.CharField(max_length=255, default='',null=False)
    order_description = models.TextField(default='')
    is_completed = models.BooleanField(default=False)

    
    def __str__(self) :
        return f"{self.user.username}:{self.name}: {self.is_completed}"
