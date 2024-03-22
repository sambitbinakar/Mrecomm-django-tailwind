from django.contrib import admin
from django.urls import path ,include,re_path
from . import views
from .views import productViewset ,authView
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
router = routers.DefaultRouter()
router.register(r'products',productViewset)

urlpatterns = [
    path('navbar/', views.navbar, name='navbar'),
    path('home/',views.home ,name='home'),
    path('api/',include(router.urls)),
    path('api/<int:pk>',views.prductdelete.as_view(),name="update"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('signup/', authView ,name="signup"),
    path('base/', views.base ,name="base" ),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)