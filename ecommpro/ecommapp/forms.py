from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



    
class UserRegister(UserCreationForm):
  username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username","class":"form-control"}))
  email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email_id","class":"form-control"}))
  password1=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password","class":"form-control"}))
  password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm password","class":"form-control"}))
  class Meta:
    model = User
    fields=['username','email']

