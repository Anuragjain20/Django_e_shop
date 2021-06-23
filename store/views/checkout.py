from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from store.models.orders import Order
# Create your views here.


class CheckOut(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for  product in products:
            order = Order(customer = Customer(id = customer),product = product,address =address,price = product.price,quantity=cart.get(str(product.id)),phone= phone)

            order.placeOrder()
        request.session['cart'] = {}   
        return redirect('cart')
