from rest_framework import serializers
from .models import Service, Intro

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','image','title','description','advantage1','advantage2','price','is_active']

class IntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intro
        fields = ['id','name','surname','profession','title','description','citation','image']