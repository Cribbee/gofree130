# coding:utf-8
from rest_framework import serializers
from .models import Luo


class LuoSerializer(serializers.Serializer):                # 它序列化的方式很类似于Django的forms
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=30, default="")

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Luo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
	instance.save()
        return instance
