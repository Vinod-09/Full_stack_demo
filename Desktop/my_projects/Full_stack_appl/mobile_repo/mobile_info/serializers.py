from rest_framework import serializers
from .models import Mobile_List, Mobile_Features

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile_Features
        fields =['id', 'battery','storage','processor']

class MobileSerializer(serializers.ModelSerializer):  
    features = FeatureSerializer(many=True, read_only=True) #get related features

    class Meta:
        model = Mobile_List
        fields = ['id','brand_name','price','features']

