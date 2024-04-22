from django.shortcuts import render,redirect
from rest_framework import viewsets,generics,status
from .models import products
from .Serializers import productserializer
from django.contrib.auth.decorators import login_required 
from rest_framework.response import Response
from .forms import UserRegister
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.models import User

# Create your views here.
def profile (request):
    return render(request,"profile.html")
def Loginview (request):
    if request.user.is_authenticated:
        return redirect("base")
    
    if request.method == "POST":
        username = request.POST.POST['username']
        password = request.POSTPOST['password']

        try:
            user = User.objects.get(username=username)
            user=authenticate(request,username=username ,password=password)

            if user is not None:
                login(request , user)
                messages.success(request, "you are login succesfully")
                return redirect("base")
            else:
                messages.warning(request , "user does not exist")
        except:
            messages.warning(request  , f"user with {username} doesn't exist")

        

    return render(request , "registration/login.html")

def LogoutView (request):
    logout(request) 
    messages.success(request,"You have been logout ") 
    return redirect('login')

def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST or None)
        if form.is_valid():
            new_user=form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f"hey{username} ,you account was created successfully")
            new_user = authenticate(username=form.cleaned_data['email'],password=form.cleaned_data['password1'] )

            login(request, new_user)
            return redirect("login")
    else:
        form = UserRegister()
    return render(request,'registration/Register.html',{'form':form})


def navbar(request):
    return render(request , 'navbar.html')
# rest api create
class productViewset(viewsets.ModelViewSet):
    queryset = products.objects.all()
    serializer_class=productserializer

    def delete(self,request, *args, **kwargs):
        products.objects.all().delete()
        return Response(status=status.HTTP_204_NO_content)
# delete the data in serializer
class prductdelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = products.objects.all()
    serializer_class=productserializer
    lookup_field = "pk"

def base (request):
    return render(request,'base.html')
 
def home(request):
    product_Detail = products.objects.all()
    return render(request , 'home.html',{'product_Detail':product_Detail})

def productview(request):
    product_Detail = products.objects.all()
    return render(request,'product.html',{'product_Detail':product_Detail})


def product_detail(request,id):
    product_object = products.objects.get(product_id=id)
    return render(request,'product_detail.html',{'product_object':product_object})
