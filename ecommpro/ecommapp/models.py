from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    categories=models.CharField(max_length=250,choices=(('Electronic','electronic'),('laptops','laptop'),('shoes','shoes'),('fashion','fashion')))
    description = models.TextField()
    price=models.IntegerField()
    date=models.DateTimeField(auto_now=True)
    image=models.ImageField()