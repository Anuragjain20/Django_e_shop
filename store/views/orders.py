

from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from store.middlewares.auth import auth_middleware

class Orders(View):


  
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        

        return render(request,'store/orders.html',{'orders':orders})
      
