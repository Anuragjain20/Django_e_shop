from django.urls import path

from .views import login,signup,home,cart,checkout,orders
from .middlewares.auth import auth_middleware


urlpatterns = [
      path('signup',signup.Signup.as_view(),name='signup'),
 path('login',login.Login.as_view(),name='login'),
  path('logout',login.logout,name='logout'),
  path('cart',cart.Cart.as_view(),name='cart'),
  path('check-out',auth_middleware(checkout.CheckOut.as_view()),name='checkout'),
  path('orders',auth_middleware(orders.Orders.as_view()),name='orders'),
    path('',home.Index.as_view(),name='homepage')
  
]
