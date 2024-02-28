from django.shortcuts import render
from rest_framework import viewsets
from .models import product
from .Serializers import productserializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
# Create your views here.
def navbar(request):
    return render(request , 'navbar.html')
class productViewset(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class=productserializer

   
def home(request):
    return render(request , 'home.html')
@login_required 
def authView(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST or None)
        if form .is_valid ():
            form.save()
    form = UserCreationForm()
    return render(request,"registration/signup.html",{"form":form})