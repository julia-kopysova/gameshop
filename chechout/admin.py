from django.contrib import admin
from .models import Order, OrderHasProduct, Delivery

class OrderHasProduct(admin.TabularInline):
    model = OrderHasProduct
    raw_id_fields = ['product']
class DeliveryAdmin(admin.ModelAdmin):
    model = Delivery
    raw_id_fields = ['user']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'delivery']
    list_filter = ['date']
    inlines = [OrderHasProduct]

admin.site.register(Order, OrderAdmin)
admin.site.register(Delivery, DeliveryAdmin)
