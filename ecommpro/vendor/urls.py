from django.urls import path
from  . import views
app_name = "vendor"

urlpatterns=[
    path('register/',views.vender_register,name="vender_register"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('create-product/',views.create_product,name="create-product"),
    path('vender_login/',views.vender_login,name='vender_login'),
    path('vender_logout/',views.vender_logout,name="vender_logout"),
    path("changepassword/",views.change_vender_password,name="vender_changePassword")
]