from django.urls import path
from . import views

urlpatterns=[
    
    path('',views. Home_page,name="Home_page"),
    path('Contact_us/',views. Contact_us,name="Contact_us"),
    path('Product_page/<products>/',views.Product_page,name="Product_page"),
    path('Product_single_page/<int:dataid>/',views.Product_single_page,name="Product_single_page"),
    path('Userlogin',views.User_login,name="User_login"),
    path('cart_page',views.cart_page,name="cart_page"),
    path('Save_to_cart/',views.Save_to_cart,name="Save_to_cart"),
    path('cart_delete/<int:dataid>/',views.cart_delete,name="cart_delete"),
    path('Save_signup_fn/',views.Save_signup_fn,name="Save_signup_fn"),
    path('User_login_fn/',views.User_login_fn,name="User_login_fn"),
    path('logout',views.user_logout,name="logout"),
    path('Save_contact',views.Save_contact,name="Save_contact"),




]
