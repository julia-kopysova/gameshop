from django.contrib import admin
from .models import Category, Product, Os, Studio

class OsAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
admin.site.register(Os, OsAdmin)

class StudioAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
admin.site.register(Studio, StudioAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'count', 'available', 'created']
    list_filter = ['available', 'name']
    prepopulated_fields = {'slug': ['name',]}
admin.site.register(Product, ProductAdmin)
