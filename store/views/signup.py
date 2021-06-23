from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import make_password, check_password









class Signup(View):
    def validateCustomer(self,customer):
        error_message = None
        if  not customer.first_name :
            error_message = 'First name Required !!'
        elif len(customer.first_name) <4:
                
            error_message = 'First name must be 4 char long'    
        if  not customer.last_name :
            error_message = 'Last name Required !!'
        elif len(customer.last_name) <4:
                
            error_message = 'last name must be 4 char long'  
        elif not customer.phone:
            error_message = 'Phone Number required'

        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char long' 

        elif len(customer.password) <6:
            error_message = 'Password must be  6 char long'
        elif len(customer.email) <4:
            error_message = 'Email must be 5 char long'          
        if customer.isExists():
            error_message = 'Email Address already registered'
        return error_message



    def get(self,request):
        return render(request,'store/signup.html')

    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name =  postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        error_message = None
        customer = Customer(first_name = first_name, last_name = last_name,phone = phone,email = email,password = password)


        value =  {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email
        }

        error_message = self.validateCustomer(customer)
                

        if not error_message:
            print(first_name,last_name,email,password)
            customer.password =  make_password(customer.password)

            customer.register()
            return redirect('homepage')
        else:
            data  = {'error' : error_message,
            'values' : value}
                    
            return  render(request,'store/signup.html',data)
