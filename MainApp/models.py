from django.db import models

PRODUCT_SIZES = (
    ("small", "S"),
    ("medium", "M"),
    ("large", "L"),
    ("xl", "XL"),
)

# Create your models here.
class CategoryDb(models.Model):
    c_name=models.CharField(null=True,blank=True,max_length=50)
    c_image=models.ImageField(upload_to="c_image")
    Description=models.CharField(null=True, blank=True,max_length=200)

class Productdb(models.Model):
    Trending=models.BooleanField(default=False)
    P_name = models.CharField(max_length=25, null=True, blank=True)
    Category = models.CharField(max_length=15, null=True, blank=True)
    p_image = models.ImageField(upload_to="p_image")
    Price = models.FloatField(null=True, blank=True,max_length=10)
    Quantity = models.CharField(max_length=20, null=True, blank=True)
    Description = models.CharField(max_length=25, null=True, blank=True)

class Options(models.Model):
    product = models.ForeignKey(Productdb, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=PRODUCT_SIZES)

class CarouserDb(models.Model):
    cover_image=models.ImageField(upload_to="cover_image")
    caption=models.CharField(null=True,blank=True,max_length=100)