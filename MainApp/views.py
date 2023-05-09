from django.shortcuts import render,redirect
from MainApp.models import CategoryDb,Productdb,CarouserDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


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
    return render(request,'Add_Product.html',{'data':data})

def save_Product(request):
     if request.method=="POST":

        pr_name = request.POST.get('Product')
        cat = request.POST.get('category')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        ds = request.POST.get('description')
        img = request.FILES['p_image']
        obj = Productdb(P_name=pr_name, Category=cat, Price=pr, Quantity=qu, Description=ds, p_image=img)
        obj.save()
        return redirect(Add_Product)
     
def Display_product(request):
    p_data = Productdb.objects.all()
    return render(request, "Display_Product.html",{'p_data': p_data})

def Edit_product(request, dataid):
    data = Productdb.objects.get(id=dataid)
    category_data = CategoryDb.objects.all()
    return render(request,"Edit_product.html", {'data':data,'category_data':category_data})

def Delete_product(request, dataid):
    data = Productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(Display_product)

def Update_product(req, dataid):
    if req.method=='POST':
        pd = req.POST.get('Product')
        ct = req.POST.get('category')
        pr = req.POST.get('price')
        qu = req.POST.get('quantity')
        ds = req.POST.get('description')
        try:
            img = req.FILES['p_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)

        except MultiValueDictKeyError:
            file = Productdb.objects.get(id=dataid).image
        Productdb.objects.filter(id=dataid).update(P_name=pd, Category=ct, Price=pr, Quantity=qu, Description=ds, p_image=file)
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
    