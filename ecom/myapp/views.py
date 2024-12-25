from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User     # for default table
from django.contrib.auth import authenticate,login,logout
from .models import Product
# Create your views here.

# index page
def index(request):
    context={}
    products=Product.objects.all()
    print(products)
    context['products']=products
    return render(request,'index.html',context)

# def index(request):
#     return render(request,'base.html')

def about(request):
    return render(request,'about.html')

# def home(request):
#     return render(request,'home.html')

def register(request):
        context={}
        if request.method == 'POST':
            e = request.POST['uemail']
            u = request.POST['username']
            p = request.POST['upassword']
            rp = request.POST['urepass']
            
            # print(e,u,p,rp)
            if e=="" or u=="" or p=="" or rp=="":
                context['error_msg']="All Fields Are Required"
                return render(request,'register.html',context)
            
            elif p != rp:
                context['error_msg']="Pasword Doesnot Match"
                return render(request,'register.html',context)
            
            elif len(p) <=8 or len(rp) <= 8:
                context['error_msg']="Pasword Contain Atleast 8 Character"
                return render(request,'register.html',context)
            
            else:
                u = User.objects.create(email=e, username=u)
                u.set_password(rp)
                u.save()
                # return HttpResponse("Data Fetched")
                return redirect('/login')
        else:
            return render(request,'register.html')

def ulogin(request):
    context={}
    if request.method == "POST":
            un = request.POST['uname']
            up = request.POST['upass']

            if un == "" or up == "":
                context['error_msg']="All Fields are Required"
                return render(request,'ulogin.html',context)
                 
                # print(un,up)

            else:
                u = authenticate(username = un,password=up)
                # print(u)
                
            
                if u!= None:
                    login(request,u)
                    return redirect('/')
                    
                else:
                    context['error_msg']="Invalid Username And Password"
                    return render(request,'ulogin.html',context)
                    
    else:
         return render(request,'ulogin.html')
    
def ulogout(request):
    logout(request)
    return redirect('/login')    

def product(request):
    return render(request,'product.html')

def cart(request):
    return render(request,'cart.html')

def cust_details(request):
    return render(request,'cust_details.html')

