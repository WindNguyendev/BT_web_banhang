from django.shortcuts import render
from .forms import PostOrder
from .models import Order
from cart.models import Cart
from django.http import HttpResponse

# Create your views here.


def Order_new(request):
    if request.method == 'POST':
        o = PostOrder(request.POST)
        if o.is_valid:
            us = request.user
            cart = Cart.objects.get(user=us)

            o_new = Order(user = us,cart = cart,name= request.POST.get('name'),phone= request.POST.get('phone'),shiping_address= request.POST.get('shiping_address'),order_description= request.POST.get('order_description'))
            o_new.save()
            return HttpResponse("successfully order")
        else:
            return HttpResponse("Nhập không đúng dữ liệu")
    else:
        return HttpResponse("Không phải request kiểu POST")


