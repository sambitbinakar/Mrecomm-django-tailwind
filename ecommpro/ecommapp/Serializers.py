from rest_framework import serializers
from .models import products
from django.contrib.auth.models import User

class productserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=products
        fields="__all__"


# class Userserializer(serializers.ModelSerializer):
#     class Meta:
#         model =User
#         fields='__all__'