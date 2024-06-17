from rest_framework import serializers
from .models import product
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)

class productserializer(TaggitSerializer,serializers.HyperlinkedModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model=product
        fields="__all__"


# class Userserializer(serializers.ModelSerializer):
#     class Meta:
#         model =User
#         fields='__all__'