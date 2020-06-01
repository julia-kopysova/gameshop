from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse
from main.models import Product
from phone_field import PhoneField
from address.models import AddressField
# Create your models here.
class Delivery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    address =  AddressField(blank=True, null=True)
    recall = models.BooleanField(default=True)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,through="OrderHasProduct", blank=False, null=False)
    delivery =  models.ForeignKey(Delivery,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('Accepted', 'Accepted'),
        ('Contacted', 'Contacted'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=9, default = 'Accepted')



class OrderHasProduct(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    def get_cost(self):
        return self.price * self.quantity
