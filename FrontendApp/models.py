from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class cartdb(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    P_name = models.CharField(max_length=25, null=True, blank=True)
    P_image = models.ImageField(upload_to="cart_image",null=True,blank=True)
    Price = models.FloatField(null=True, blank=True,max_length=10)
    Total_price=models.FloatField(null=True,blank=True,max_length=10)
    Quantity = models.CharField(max_length=20, null=True, blank=True)



    
