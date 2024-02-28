from django.contrib import admin
from django.urls import path ,include
from . import views
from .views import productViewset ,authView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products',productViewset)

urlpatterns = [
    path('navbar/', views.navbar, name='navbar'),
    path('home/',views.home ,name='home'),
    path('',include(router.urls)),
    path("accounts/", include("django.contrib.auth.urls")),
    path('signup/', authView ,name="signup")
]