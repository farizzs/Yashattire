from django.urls import path
from . import views

urlpatterns=[
    path('Home_page/',views. Home_page,name="Home_page"),
    path('Contact_us/',views. Contact_us,name="Contact_us"),
    path('Product_page/<products>/',views.Product_page,name="Product_page")
]