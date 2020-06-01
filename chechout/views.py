from django.shortcuts import render,reverse
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from .models import Order, OrderHasProduct, Delivery
from cart.cart import Cart
from .forms import DeliveryForm
import logging, logging.config
import sys
LOGGING = {
'version': 1,
'handlers': {
    'console': {
        'class': 'logging.StreamHandler',
        'stream': sys.stdout,
    }
},
'root': {
    'handlers': ['console'],
    'level': 'INFO'
}
}
logging.config.dictConfig(LOGGING)
# Create your views here.

def create_order(request):
    form = DeliveryForm(request.POST)
    logging.info(form)
    user = request.user
    cart = Cart(request)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            delivery = Delivery(user = user,  recall = cd['recall'], address_devivery = cd['address'], phone = cd['phone'])
            delivery.save()
            total_price = cart.get_total_price()
            o = Order(user = user, delivery = delivery )
            o.save()
            for i in cart:
                order_has_product = OrderHasProduct.objects.create(order=o, product=i['product'] , price=i['price'], quantity=i['quantity'], amount = total_price)
            cart.clear()
            return render(request,'success.html', { 'order': o })
            #redirect('success')
        else:
            form = CartAddItemForm(request.POST)
    return render(request,'checkout.html', { 'form': form })

#def display_info(request):
    #user = request.user
    #o = get_object_or_404(Order, user = user)
    #return render(request,'success.html', { 'order': o })
