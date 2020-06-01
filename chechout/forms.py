from django import forms
from phone_field import PhoneField

class DeliveryForm(forms.Form):
    phone = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)
    recall = forms.BooleanField()
