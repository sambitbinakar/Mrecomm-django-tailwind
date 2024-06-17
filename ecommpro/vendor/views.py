from django.shortcuts import render,redirect
from .models import vender,product
from .forms import product_form,venderResigter
from django.contrib import messages
# Create your views here.

def dashboard(request):
    return render(request,"vender/dashboard.html")

def create_product(request):
    if request.method == 'POST':
        productform = product_form(request.POST or None)
        if productform.is_valid():
            productform.save()
            return redirect('dashboard')
    productform = product_form()
    return render(request,"create_product.html",{'productform':productform})
  

def vender_register(request):
    if request.method == "POST":
        venderform = venderResigter(request.POST or None)
        if venderform.is_valid():
            new_user = venderform.save()
            username=venderform.cleaned_data.get("username")
            messages.success(request,f"hey{username} ,you account was created successfully")
            # new_user = (username=venderform.cleaned_data['email'],password=venderform.cleaned_data['password1'] )

            return redirect("dashboard")
    else:
        venderform = venderResigter()

    return render(request,"vender-register.html",{'venderform':venderform})