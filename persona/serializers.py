# coding:utf-8
from rest_framework import serializers
from .models import Scenic

class ScenicSerializer(serializers.Serializer):                # 它序列化的方式很类似于Django的forms
    
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    user_name = serializers.CharField()
    user_lv = serializers.IntegerField()
    view_name = serializers.CharField()
    view_id = serializers.IntegerField()
    city_id = serializers.IntegerField()
    created = serializers.DateTimeField(default="")
    updated = serializers.DateTimeField(default="")
    pts = serializers.FloatField(default="")
    TYPE_CHOICES = (('0','firstTime'),('1','recommend'),('2','feedBack'))
    type = serializers.CharField(default="")


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Scenic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.user_lv = validated_data.get('user_lv', instance.user_lv)
        instance.view_id = validated_data.get('view_id', instance.view_id)
        instance.view_name = validated_data.get('view_name', instance.view_name)
        instance.city_id = validated_data.get('city_id', instance.city_id)
        instance.created = validated_data.get('created', instance.created)
        instance.updated = validated_data.get('updated', instance.updated)
        instance.pts = validated_data.get('pts', instance.pts)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance
