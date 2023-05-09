from django.shortcuts import render
from MainApp.models import CategoryDb,CarouserDb,Productdb

# Create your views here.
def Home_page(request):
    c_data=CategoryDb.objects.all()
    cr_data=CarouserDb.objects.all()
    return render(request,"Home_Page.html",{'c_data':c_data,'cr_data':cr_data})

def Contact_us(request):
    return render(request,"Contact_us.html")


def Product_page(request,products):
    data=CategoryDb.objects.all()
    product_data=Productdb.objects.filter(Category=products)
    return render(request,"product_page.html",{'data':data,'product_data':product_data})

def Product_single_page(request,dataid):
    data=CategoryDb.objects.all()
    product=Productdb.objects.get(id=dataid)
    return render(request, "product_single.html",{'data':data,'product':product})
    

