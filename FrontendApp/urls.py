from django.urls import path
from . import views

urlpatterns=[
    path('Home_page/',views. Home_page,name="Home_page"),
    path('Contact_us/',views. Contact_us,name="Contact_us"),
    path('Product_page/<products>/',views.Product_page,name="Product_page"),
    path('Product_single_page/<int:dataid>/',views.Product_single_page,name="Product_single_page"),
    path('User_login/',views.User_login,name="User_login"),
    path('cart_page',views.cart_page,name="cart_page"),
    path('Save_to_cart/',views.Save_to_cart,name="Save_to_cart"),
    path('cart_delete/<int:dataid>/',views.cart_delete,name="cart_delete"),
    path('Save_signup_fn/',views.Save_signup_fn,name="Save_signup_fn"),
    path('User_login_fn/',views.User_login_fn,name="User_login_fn"),
    


]
