from django.shortcuts import render,redirect
from ecommapp.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import datetime
from django.db.models import Sum
# Create your views here.

def dashboard(request):
    revenue = CartOrder.objects.aaggregate(price = Sum("price"))
    total_orders_count = CartOrder.objects.all()
    all_products = product.objects.all()
    all_catagories = catagories.objects.all()
    new_customers = User.objects.all().order_by("-id")
    latest_order  =CartOrder.objects.all()
    this_month = datetime.datetime.now()
    monthly_income = CartOrder.objects.filter(order_date = this_month).aaggregate(price = Sum("price"))
    context ={
        "revenue": revenue,
        "total_orders_count":total_orders_count,
        "all_products":all_products,
        "all_catagories":all_catagories,
        "new_customers":new_customers,
        "latest_order":latest_order,
        "monthly_income":monthly_income,
    }
    return render(request,"dashboard.html",context)

def create_product(request):
    if request.method == 'POST':
        productform = product_form(request.POST or None)
        if productform.is_valid():
            new_product = productform.save(commit=False)
            new_product.vendor = vender.objects.get(user = request.vender)
            productform.save_m2m()
            return redirect('dashboard')
    else:
        productform = product_form()


    return render(request,"create_product.html",{'productform':productform})
  

def vender_register(request):
    if request.method == "POST":
        venderform = venderResigter(request.POST or None)
        if venderform.is_valid():
            venderform.save()
            return redirect("dashboard")
    else:
        venderform = venderResigter()

    return render(request,"vender-register.html",{'venderform':venderform})

def vender_login(request):
    if request.method == 'POST':
        login_form = vender_login_form(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            seller = authenticate(request,email=email,password=password)
            if seller is not None:
                login(request,seller)
                return redirect('dashboard')
    else:
        login_form = vender_login_form()
    return render(request,'Vender_login.html',{'login_form':login_form})


def vender_logout(request):
    logout(request)
    return redirect('vender_register')

def change_vender_password(request):
    if request.method == 'POST':
        password_form = venderPasswordchange(request.post)
        if password_form.is_valid():
            seller = request.user
            if seller.check_password(password_form.cleaned_data['old_password']):
                seller.set_password(password_form.cleaned_data['new_password'])
                seller.save()
                return redirect('dashbord')
    else:
        password_form = venderPasswordchange()
    return render(request,'change_vender_password.html',{'password_form':password_form})