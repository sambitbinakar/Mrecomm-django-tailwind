from django import forms
from ecommapp.models import vender,product

class product_form(forms.ModelForm):
  class Meta:
    model = product
    fields ="__all__"

class venderResigter(forms.Form):
  username =forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","class": "form-control"}))
  email =forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email-Id","class": "form-control"}))
  mobileno= forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Mobile NO","class": "form-control"}))
  password1 =forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","class": "form-control"}))
  password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Rewrite-password","class": "form-control"}))
  GSTNo = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"GST-No","class": "form-control"}))
  PanCard_No =forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Pancard_No","class": "form-control"}))
  class Meta:
    model = vender
    fields="__all__"