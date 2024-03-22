from django.shortcuts import render
from rest_framework import viewsets,generics,status
from .models import products
from .Serializers import productserializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from rest_framework.response import Response

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
    products = products.objects.all()
    return render(request , 'home.html',{'products':products})

def authView(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST or None)
        if form .is_valid ():
            form.save()
    form = UserCreationForm()
    return render(request,"registration/signup.html",{"form":form})