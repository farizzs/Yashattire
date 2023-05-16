from django.db import models

# Create your models here.
class cartdb(models.Model):
    P_name = models.CharField(max_length=25, null=True, blank=True)
    p_image = models.ImageField(upload_to="cart_image")
    Price = models.FloatField(null=True, blank=True,max_length=10)
    Quantity = models.CharField(max_length=20, null=True, blank=True)
    
