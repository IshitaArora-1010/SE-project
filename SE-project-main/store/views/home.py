from django.shortcuts import render
from store.models.product import Product

def index(request):
    products_slider = Product.objects.all().order_by('-ids')[:4]
    return render(request, 'home.html')
