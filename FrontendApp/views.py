from django.shortcuts import render,redirect
from MainApp.models import CategoryDb,CarouserDb,Productdb,Options

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
    options =Options.objects.filter(product=product)

    return render(request, "product_single.html",{'data':data,'product':product,'options':options})


def Save_to_cart(request):
     if request.method=="POST":

        pr_name = request.POST.get('p_name')
        sizes = request.POST.getlist('sizes')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        img = request.FILES['p_image']
        obj = Productdb(P_name=pr_name, Price=pr, Quantity=qu,  p_image=img)
        obj.save()
        for size in sizes:
            Options.objects.create(product=obj, size=size)
        return redirect(Save_to_cart)

def User_login(request):
    return render(request,"user_login.html")


    

