from django.contrib import admin
from django.urls import path ,include
from  . import views
from ecommapp.views import productViewset
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
router = routers.DefaultRouter()
router.register(r'products',productViewset)

urlpatterns = [
    path('navbar/', views.navbar, name='navbar'),
    path('',views.home ,name='home'),
    path('register/',views.register ,name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("profile/",views.profile , name='profile'),
    path('api/',include(router.urls)),
    path('api/<int:pk>',views.prductdelete.as_view(),name="update"),
    path('product/',views.productview,name='product'),
    path('<int:id>/',views.product_detail,name='product-detail'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)