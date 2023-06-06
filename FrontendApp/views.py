from django.shortcuts import render,redirect
from MainApp.models import CategoryDb,CarouserDb,Productdb,Options
from FrontendApp.models import cartdb,ContactDb
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home_page(request):
    c_data=CategoryDb.objects.all()
    cr_data=CarouserDb.objects.all()
    trending_products=Productdb.objects.filter(Trending=True)
    return render(request,"Home_Page.html",{'c_data':c_data,'cr_data':cr_data,"trending_products":trending_products})

def Contact_us(request):
    data=CategoryDb.objects.all()
    return render(request,"Contact_us.html",{'data':data})


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
    data=CategoryDb.objects.all()
    cart_data=cartdb.objects.filter(user=request.user)
    context={
        'data':data,
        "cart_data":cart_data
    }
    return render(request, "cart_page.html",context)

@login_required(login_url='/Userlogin')
def Save_to_cart(request):
    if request.method=="POST":
        product_id=request.POST.get('product')
        product=Productdb.objects.get(id=product_id)
        quantity = request.POST.get('Qty')
      
        total_price = request.POST.get('totalprice')
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
                context["error"] = "This Username alraedy exists"
                return render(request,"user_login.html",context)
            if  User.objects.filter(email=emailid).exists():
                context["error"] = "This Email alraedy exists"
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
         
def User_login_fn(request):
    if request.method == 'POST':
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        user = authenticate(username=username_r, password=password_r)
        if user is not None:
            login(request=request, user=user)
          
            return redirect(Home_page)
        else:
            return redirect(User_login)

def user_logout(request):
    logout(request)
    return redirect(Home_page)
         
def Save_contact(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact_data=ContactDb(Name=name,Email=email,Subject=subject,Message=message)
        contact_data.save()
        return redirect(Contact_us)
    
def All_Products(request):
    data=CategoryDb.objects.all()
    product_data=Productdb.objects.all()
    context={
        'data':data,
        'product_data':product_data
    }
    return render(request,"All_products.html",context)





         


    

