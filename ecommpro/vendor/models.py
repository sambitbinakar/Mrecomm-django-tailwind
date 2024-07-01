from django.db import models
from shortuuid.django_fields import ShortUUIDField
# Create your models here.

def user_directory_path(instance,filename):
    return 'user_(0)/(1)'.format(instance.user.id,filename)


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