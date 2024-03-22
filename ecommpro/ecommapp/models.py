from django.db import models

# Create your models here.
class products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    categories=models.CharField(max_length=250,choices=(('Electronic','electronic'),('Fashion','Fashion'),('Grocery','Grocery'),('Home & Furniture','Home & furniture'),('Mobiles','mobiles'),('Appliances','Appliance')))
    description = models.TextField()
    price=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='Image/uploads')

    def __str__(self):
        return self.name
    