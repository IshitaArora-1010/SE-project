from django.shortcuts import redirect, render
from django.views import View
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def get(self, request):
        if (request.session.get('cart') == None):
            return render(request, 'cart.html')
        else:
            ids = list(request.session.get('cart').keys())
            print("ids:", ids)
            products = Product.get_products_by_id(ids)
            return render(request, 'checkout.html', {'products': products})

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          name=name,
                          email=email,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')

