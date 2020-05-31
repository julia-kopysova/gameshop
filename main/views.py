from django.shortcuts import render,reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.views.generic import ListView,DetailView
from cart.forms import CartAddProductForm


def product_list(request, slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request,'catalog.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id):
    cart_product_form = CartAddProductForm()
    product = get_object_or_404(Product,id=id,available=True)
    return render(request, 'product.html',  {'product': product, 'cart_form':cart_product_form})
