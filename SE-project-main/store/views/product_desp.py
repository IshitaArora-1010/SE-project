from django.shortcuts import render
from store.models.product import Product
from store.models.category import Category

def product_detail(request):

    productID = request.GET.get('product')
    products = Product.get_products_by_id(productID)
    data={}
    data['product'] = products
    return render(request, 'description.html', data)
