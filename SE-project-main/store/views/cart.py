from django.shortcuts import render
from store.models.product import Product
from django.views import View

class Cart(View):
    def get(self, request):
        if(request.session.get('cart')==None):
            return render(request, 'cart.html')
        else:
            ids = list(request.session.get('cart').keys())
            print("ids:",ids)
            products = Product.get_products_by_id(ids)
            return render(request, 'cart.html', {'products': products})
