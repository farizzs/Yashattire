from django.shortcuts import render,redirect
from MainApp.models import CategoryDb,CarouserDb,Productdb,Options
from FrontendApp.models import cartdb,ContactDb,CheckOut, Order
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# Create your views here.
def Home_page(request):
    c_data=CategoryDb.objects.all()
    cr_data=CarouserDb.objects.all()
    trending_products=Productdb.objects.filter(Trending=True)
    New_arrival=Productdb.objects.filter(New_Arival=True)
    return render(request,"Home_Page.html",{'c_data':c_data,'cr_data':cr_data,"trending_products":trending_products,'New_arrival':New_arrival})

def Contact_us(request):
    data=CategoryDb.objects.all()
    return render(request,"Contact_us.html",{'data':data})


def Product_page(request,products):
    data=CategoryDb.objects.all()
    product_data=Productdb.objects.filter(Category=products)
    return render(request,"product_page.html",{'data':data,'product_data':product_data})

def Product_single_page(request,dataid):
    already="False"
    data=CategoryDb.objects.all()
    product=Productdb.objects.get(id=dataid)
    options =Options.objects.filter(product=product)
    this_category=product.Category
    this_category_products=Productdb.objects.filter(Category=this_category)
    if cartdb.objects.filter(P_name=product.P_name, user=request.user).exists():
        already="True"
    return render(request, "product_single.html",{'data':data,'product':product,'options':options,'this_category_products':this_category_products,'already':already})



def cart_page(request):
    data=CategoryDb.objects.all()
    cart_data=cartdb.objects.filter(user=request.user)
    grant_total = cart_data.aggregate(Sum("Total_price"))["Total_price__sum"]
    context={
        'data':data,
        "cart_data":cart_data,
        "grant_total":grant_total
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

def Checkout(request):
    data=CategoryDb.objects.all()
    cart_datas=cartdb.objects.filter(user=request.user)
    grant_total = cart_datas.aggregate(Sum("Total_price"))["Total_price__sum"]
    return render(request,"checkOutpage.html",{'data':data,'cart_datas':cart_datas,'grant_total':grant_total})

def Save_checkout(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        city=request.POST.get('city')
        pin=request.POST.get('pin_code')
        order = Order.objects.create(
            user=request.user
        )
        data=cartdb.objects.filter(user=request.user)
        creation_data = [
                CheckOut(
                    order=order,
                    Name=name,
                    Email=email,
                    Mobile=mobile,
                    Address=address,
                    City=city,
                    Pin_Code=pin,
                    Product_name=cart_item.P_name,
                    Quantity=cart_item.Quantity,
                    Total_price=cart_item.Total_price,
                )
                for cart_item in data

            ]
        print(creation_data)
        CheckOut.objects.bulk_create(creation_data)  
        data.delete()
        return redirect(Home_page)
    
def Invoice(request):
    return render(request,'invoice.html')

def Order_page(request):
    return render(request,"Myorder.html")








         


    

