from django.db import models

# Create your models here.
class catagories(models.Model):
    name=models.CharField(max_length=200)
    image=models.CharField(max_length=250)
    def  __str__(self):
        return self.name


class products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    categories=models.CharField(max_length=250,choices=(('Electronic','electronic'),('Fashion','Fashion'),('Grocery','Grocery'),('Home & Furniture','Home & furniture'),('Mobiles','mobiles'),('Appliances','Appliance'),('watches','watches')))
    description = models.TextField()
    price=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now=True)
    image=models.CharField(max_length=200)
    sale = models.BooleanField(default=False)
    saleprice = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    