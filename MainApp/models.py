from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    c_name=models.CharField(null=True,blank=True,max_length=50)
    c_image=models.ImageField(upload_to="c_image")
    Description=models.CharField(null=True, blank=True,max_length=200)

class Productdb(models.Model):
    P_name = models.CharField(max_length=25, null=True, blank=True)
    Category = models.CharField(max_length=15, null=True, blank=True)
    p_image = models.ImageField(upload_to="p_image")
    Price = models.FloatField(null=True, blank=True,max_length=10)
    Quantity = models.CharField(max_length=20, null=True, blank=True)
    Description = models.CharField(max_length=25, null=True, blank=True)

class CarouserDb(models.Model):
    cover_image=models.ImageField(upload_to="cover_image")
    caption=models.CharField(null=True,blank=True,max_length=100)