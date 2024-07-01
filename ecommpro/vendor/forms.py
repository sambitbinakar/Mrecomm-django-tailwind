from django import forms
from ecommapp.models import vender,product

class product_form(forms.ModelForm):
  name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"product name","class": "form-control"}))
  class Meta:
    model = product
    fields =["name","categories","image","price","saleprice","image","sale","In_stock",'featured',"description"]

class venderResigter(forms.ModelForm):
  username =forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","class": "form-control"}))
  email =forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email-Id","class": "form-control"}))
  image = forms.ImageField()
  mobileno= forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Mobile NO","class": "form-control"}))
  password1 =forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","class": "form-control"}))
  password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"confirm-password","class": "form-control"}))
  GSTNo = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"GST-No","class": "form-control"}))
  PanCard_No =forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Pancard_No","class": "form-control"}))
  class Meta:
    model = vender
    fields="__all__"

  def clean_password(self):
      password = self.cleaned_data.get("password1")
      confirm_password = self.cleaned_data.get("password2")
      if password and confirm_password and password != confirm_password:
          raise forms.ValidationError("Passwords don't match")
      return confirm_password
  def save(self, commit=True):
        seller = super().save(commit=False)
        seller.set_password(self.cleaned_data["password1"])
        if commit:
            seller.save()
        return seller

class vender_login_form(forms.Form):
   email = forms.EmailField(widget=forms.EmailInput)
   password = forms.CharField(widget=forms.PasswordInput)


class venderPasswordchange(forms.Form):
  old_password = forms.CharField(widget=forms.PasswordInput)
  new_password = forms.CharField(widget=forms.PasswordInput)
  confirm_new_password = forms.CharField(widget=forms.PasswordInput)
   
  def clean(self):
   cleaned_data = super().clean()
   new_password = cleaned_data.get('new_password')
   confirm_new_password = cleaned_data.get('confirm_new_password')
   if new_password and confirm_new_password and new_password != confirm_new_password:
      raise forms.ValidationError("password don't match")
   return cleaned_data