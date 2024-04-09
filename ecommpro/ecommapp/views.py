from django.shortcuts import render
from rest_framework import viewsets,generics,status
from .models import products
from .Serializers import productserializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.


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

# def register(UserCreationForm):
#     if request.method =="POST":
#         form = UserCreationForm(request.POST or None)
#         if form .is_valid ():
#             form.save()
#     form = UserCreationForm()
#     return render(request,"registration/Register.html",{"form":form})

def productview(request):
    product_Detail = products.objects.all()
    return render(request,'product.html',{'product_Detail':product_Detail})


def product_detail(request,id):
    product_object = products.objects.get(product_id=id)
    return render(request,'product_detail.html',{'product_object':product_object})