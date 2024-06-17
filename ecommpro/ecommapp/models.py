from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from  taggit.managers import TaggableManager

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
def user_directory_path(instance,filename):
    return 'user_(0)/(1)'.format(instance.user.id,filename)

class catagories(models.Model):
    cid = ShortUUIDField( length=10,
        max_length=20,
        prefix="cat_",
        alphabet="abcdefg1234",
        primary_key=True)
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="catagory")

    class Meta:
        verbose_name_plural ="catagories"

    def  __str__(self):
        return self.name
    
class tags(models.Model):
    pass

class vender(models.Model):
    vid= ShortUUIDField(length=16,
        max_length=20,
        prefix="pr_",
        alphabet="abcdefghigklm1234",
        unique=True)
    Name = models.CharField(max_length=200)
    image =models.ImageField(upload_to=user_directory_path)
    PanCard_No=models.CharField(max_length=200,default="ABCD23456")
    GSTNo =models.CharField(max_length=200,default="ABCD23456")
    Address = models.CharField(max_length=200)
    mobileno = models.IntegerField(default="917869433434")
    shipping_time = models.CharField(max_length=200)
    authentic_rating = models.CharField(max_length=200)
    days_return = models.CharField(max_length=200)


class product(models.Model):
    product_id = ShortUUIDField( length=10,
        max_length=20,
        prefix="pr_",
        alphabet="abcdefg1234",
        unique=True)
    user = models.ForeignKey(vender,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=250)
    categories=models.ForeignKey(catagories,on_delete=models.SET_NULL,null=True)
    description = models.TextField(null=True,blank=True)
    price=models.IntegerField()
    saleprice = models.IntegerField()
    date=models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(null=True,blank=True)
    image=models.CharField(max_length=200)
    sale = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)
    status = models.BooleanField(default=True)
    In_stock= models.BooleanField(default=True)
    featured =models.BooleanField(default= False)


    def get_percentage (self):
        new_price=(self.price/self.saleprice)*100
        return new_price
    
    def __str__(self):
        return self.name
   
 # choices=('Electronic','electronic'),('Fashion','Fashion'),('Grocery','Grocery'),('Home & Furniture','Home & furniture'),('Mobiles','mobiles'),('Appliances','Appliance'),('watches','watches'),('AudioDevice','Audiodevice'))   

class CartOrder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price  = models.CharField(max_length=100,default=0000)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE , max_length=30,default="Processing")

    class Meta:
        verbose_name_plural = "cart Order"

    def __str__(self):
        return self.user

class cartOrderItem(models.Model):
    order = models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    invoice_no= models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.CharField(max_length=100)
    total = models.CharField(max_length=100)   


    class Meta:
        verbose_name_plural = "Cart Oder Item"

    def order_img(self):
        return mark_safe('<img src="static/image/catagory/" width="50" height="50"/>'%(self.image))
    
    def __str__(self):
        return self.order.user

#order (review wislist address)

class productReview(models.Model):
    user = models.ForeignKey(User ,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(product,on_delete=models.SET_NULL,null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING,default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product_reviews"

    def __str__(self) :
        return self.product.name
    
    def get_rating(self):
        return self.rating
    
class wishlist(models.Model):
    user = models.ForeignKey(User ,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(product,on_delete=models.SET_NULL,null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "wishlist"

    def __str__(self) :
        return self.product.name
    


class Address(models.Model):
    user = models.ForeignKey(User ,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=200,null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Address"