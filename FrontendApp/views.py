from django.shortcuts import render,redirect
from MainApp.models import CategoryDb,CarouserDb,Productdb,Options
from FrontendApp.models import cartdb
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

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

def cart_page(request):
    cart_data=cartdb.objects.filter(user=request.user)
    context={
        "cart_data":cart_data
    }
    return render(request, "cart_page.html",context)


def Save_to_cart(request):
    if request.method=="POST":
        product_id=request.POST.get('product')
        product=product=Productdb.objects.get(id=product_id)
        quantity = request.POST.get('Qty')
      
        total_price = float(quantity) * float(product.Price)
        obj = cartdb(P_name=product.P_name, Price=product.Price, Quantity=quantity, Total_price=total_price, P_image=product.p_image,user=request.user)
        obj.save()
    return redirect(cart_page)

    
def cart_delete(request,dataid):
    data=cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cart_page)
    

def User_login(request):
    return render(request,"user_login.html")

def Save_signup_fn(request):
     if request.method=="POST":
         try:
            context = {}
            username=request.POST.get('username')
            emailid=request.POST.get('emailid')
            password=request.POST.get('password')
            confirm_user=request.POST.get('password2')
            if User.objects.filter(username=username).exists():
                context["error"] = "This user name alraedy exists"
                return render(request,"user_login.html",context)
            if password != confirm_user:
                context["error"] = "Passwords not same"
                return render(request,"user_login.html",context)
            User.objects.create_user(username=username,email=emailid,password=password)
         
            return render(request,"user_login.html",context)
         except Exception as e:
            context = {
               "error":str(e)
            }
            return render(request,"user_login.html",context)
         
def User_login_fn(req):
    if req.method == 'POST':
        username_r = req.POST.get("username")
        password_r = req.POST.get("password")
        user = authenticate(username=username_r, password=password_r)
        if user is not None:
            login(request=req, user=user)
            return redirect(Home_page)
        else:
            return redirect(User_login)
         

         


    

