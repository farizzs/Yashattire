from django.shortcuts import render,redirect
from MainApp.models import CategoryDb,Productdb,CarouserDb
from FrontendApp.models import ContactDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from . models import PRODUCT_SIZES, Options


# Create your views here
def Homepage(request):
    return render(request,'Admin_homepage.html')
def AddCategory(request):
    return render(request,'Add_Categories.html')
def SaveCategory(request):
    if request.method=="POST":
        name=request.POST.get('c_name')
        image=request.FILES['c_image']
        description=request.POST.get('description')
        category_data=CategoryDb(c_name=name,c_image=image,Description=description)
        category_data.save()
        return redirect(AddCategory)
    
def DisplayCategory(request):
    c_data=CategoryDb.objects.all()
    return render(request, "Display_Category.html",{'c_data':c_data})

def editcategory(request,dataid):
    data=CategoryDb.objects.get(id=dataid)
    print(data)
    return render(request,"Edit_category.html",{'data':data})

def delete_category(request,dataid):
    data=CategoryDb.objects.filter(id=dataid)
    data.delete()
    return redirect(DisplayCategory)

def update_category(request, dataid):
    if request.method=='POST':
        na = request.POST.get('c_name')
        des = request.POST.get('description')
        try:
            img = request.FILES['c_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)

        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=dataid).c_image
        CategoryDb.objects.filter(id=dataid).update(c_name=na, Description=des, c_image=file)
        return redirect(DisplayCategory)
    

def admin_login(request):
    return render(request,"admin_loginpage.html")


def adminlogin_fn(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(Homepage)
            else:
                return redirect(admin_login)
            
        else:
            return redirect(adminlogin_fn)
        
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)


def Add_Product(request):
    data=CategoryDb.objects.all()
    context={
        "data":data,
        "sizes":PRODUCT_SIZES
    }
    return render(request,'Add_Product.html',context)

def save_Product(request):
     if request.method=="POST":

        pr_name = request.POST.get('Product')
        cat = request.POST.get('category')
        sizes = request.POST.getlist('sizes')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        ds = request.POST.get('description')
        img = request.FILES['p_image']
        trendy = request.POST.get('trendy')
        
        obj = Productdb(P_name=pr_name, Category=cat, Price=pr, Quantity=qu, Description=ds, p_image=img, Trending=True if trendy=="yes" else False)
        print("nooo",trendy)
        obj.save()
        for size in sizes:
            Options.objects.create(product=obj, size=size)
        return redirect(Add_Product)
     
def Display_product(request):
    p_data = Productdb.objects.all()
    return render(request, "Display_Product.html",{'p_data': p_data})

def Edit_product(request, dataid):
    data = Productdb.objects.get(id=dataid)
    category_data = CategoryDb.objects.all()
    sizes=PRODUCT_SIZES
    return render(request,"Edit_product.html", {'data':data,'category_data':category_data,'sizes':sizes})

def Delete_product(request, dataid):
    data = Productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(Display_product)

def Update_product(req, dataid):
    if req.method=='POST':
        pd = req.POST.get('Product')
        ct = req.POST.get('category')
        sizes = req.POST.getlist('sizes')
        pr = req.POST.get('price')
        qu = req.POST.get('quantity')
        ds = req.POST.get('description')
        try:
            img = req.FILES['p_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)

        except MultiValueDictKeyError:
            file = Productdb.objects.get(id=dataid).image
        obj = Productdb.objects.get(id=dataid)
        obj.P_name = pd
        obj.Category = ct
        obj.Price = pr
        obj.Quantity = qu
        obj.Description = ds
        obj.p_image = file
        obj.save()
        Options.objects.filter(product=obj).delete()
        for size in sizes:
            Options.objects.create(product=obj, size=size)
        return redirect(Display_product)
    

def Add_Carousel(request):
    return render(request,'Add_Carousel_img.html')

def SaveCarousel(request):
    if request.method=="POST":
        image=request.FILES['cr_image']
        cap=request.POST.get('caption')
        carousel_data=CarouserDb(cover_image=image,caption=cap)
        carousel_data.save()
        return redirect(Add_Carousel)
    
def DisplayCarousel(request):
    cr_data=CarouserDb.objects.all()
    return render(request,"Display_Carousel.html",{'cr_data':cr_data})

def Edit_Carousel(request,dataid):
    data=CarouserDb.objects.get(id=dataid)
    print(data)
    return render(request,"Edit_Carousel.html",{'data':data})

def delete_carousal(request,dataid):
    data=CarouserDb.objects.filter(id=dataid)
    data.delete()
    return redirect(DisplayCarousel)

def update_Carousel(request, dataid):
    if request.method=='POST':
        cap = request.POST.get('caption')
        try:
            img = request.FILES['cr_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)

        except MultiValueDictKeyError:
            file = CarouserDb.objects.get(id=dataid).c_image
        CarouserDb.objects.filter(id=dataid).update(caption=cap, cover_image=file)
        return redirect(DisplayCarousel)
    
def Display_contact(request):
    data=ContactDb.objects.all()
    context={
        'data':data
    }
    return render(request,"Display_contact_deatails.html",context)

def Delete_contact(request,dataid):
    data= ContactDb.objects.filter(id=dataid)
    data.delete()
    return redirect(Display_contact)

def Display_customers(request):
    data=User.objects.all()
    context={
        'data':data
    }
    return render(request, "Display_Customers.html",context)

def Delete_customers(request,dataid):
    data = User.objects.filter(id=dataid)
    data.delete()
    return redirect(Display_customers)
