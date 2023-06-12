from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class cartdb(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    P_name = models.CharField(max_length=25, null=True, blank=True)
    P_image = models.ImageField(upload_to="cart_image",null=True,blank=True)
    Price = models.FloatField(null=True, blank=True,max_length=10)
    Total_price=models.FloatField(null=True,blank=True,max_length=10)
    Quantity = models.CharField(max_length=20, null=True, blank=True)

class ContactDb(models.Model):
    Name= models.CharField(null=True,blank=True,max_length=100,unique=True)
    Email= models.EmailField()
    Subject=models.CharField(null=True,blank=True,max_length=100)
    Message=models.CharField(null=True,blank=True, max_length=1000)

ORDER_STATUS = (
    ("Pending", "Pending"),
    ("Placed", "Placed"),
    ("Cancelled", "Cancelled"),
    ("Delivered", "Delivered"),

)

class Order(models.Model):
    status=models.CharField(max_length=20, choices=ORDER_STATUS ,default="Pending")
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    invoice_id = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def save(self, **kwargs):
        if not self.pk:
            self.invoice_id = f"YA-INV-{datetime.now()}_{self.user.id}"
            self.order_id = f"YA-ORD-{datetime.now()}_{self.user.id}"
        return super().save(**kwargs)


class CheckOut(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name="order_checkouts")
    Name= models.CharField(null=True,blank=True,max_length=100)
    Email=models.EmailField()
    Mobile=models.IntegerField()
    Address=models.CharField(null=True,blank=True,max_length=100)
    City=models.CharField(max_length=100)
    Pin_Code=models.IntegerField()
    Product_name=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    Total_price=models.IntegerField(null=True,blank=True)








    
