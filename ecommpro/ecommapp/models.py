from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.html import mark_safe
STATUS_CHOICE={
    ("process","Processed"),
    ("shipped","Shipped"),
    ("delivered","Delivered"),
}
RATING={
    (1,"★☆☆☆☆"),
    (2,"★★☆☆☆"),
    (3,"★★★☆☆"),
    (4,"★★★★☆"),
    (5,"★★★★★"),
}

class catagories(models.Model):
    cid = models.UUIDField(editable=False,primary_key=True, max_length=10)
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="catagory")

    class Meta:
        verbose_name_plural ="catagories"

    def  __str__(self):
        return self.name
class tags(models.Model):
    pass

class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    categories=models.ForeignKey(catagories,on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    price=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now=True)
    image=models.CharField(max_length=200)
    sale = models.BooleanField(default=False)
    saleprice = models.CharField(max_length=100)
    tags =models.ForeignKey(tags,on_delete=models.SET_NULL,null=True)
    status = models.BooleanField(default=True)
    in_stock    = models.BooleanField(default=True)
    featured =models.BooleanField(default= False)

    def __str__(self):
        return self.name
    def get_percentage (self):
        new_price=(self.price/self.saleprice)*100
        return new_price
 # choices=('Electronic','electronic'),('Fashion','Fashion'),('Grocery','Grocery'),('Home & Furniture','Home & furniture'),('Mobiles','mobiles'),('Appliances','Appliance'),('watches','watches'),('AudioDevice','Audiodevice'))   

class CartOrder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price  = models.CharField(max_length=100,default=0000)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE , max_length=30,default="Processing")

    class Meta:
        verbose_name_plural = "cart Order"


class cartOrderItem(models.Model):
    order = models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.CharField(max_length=100)
    total = models.CharField(max_length=100)   


    class Meta:
        verbose_name_plural = "Cart Oder Item"

    def order_img(self):
        return mark_safe('<img src="/static/image/ width="50" height="50"/>'%(self.image))
    

#oder review wislist address

class product