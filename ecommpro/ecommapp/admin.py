from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(vender)
admin.site.register(product)
admin.site.register(catagories)
admin.site.register(cartOrderItem)
admin.site.register(productReview)
admin.site.register(wishlist)
admin.site.register(Address)

