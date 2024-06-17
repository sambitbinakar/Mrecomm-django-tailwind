from django.urls import path ,include
from  . import views

urlpatterns=[
    path('register',views.vender_register,name="register"),
    path('dashboard',views.dashboard,name="dashboard")
]