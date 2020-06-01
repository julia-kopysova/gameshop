from django import forms
from address.forms import AddressField
from phone_field import PhoneField

class DeliveryForm(forms.Form):
    #phone = PhoneField(blank = True)
    #address = AddressField(blank = True)
    recall = forms.BooleanField()
