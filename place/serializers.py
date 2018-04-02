# coding:utf-8
from rest_framework import serializers
from .models import View

class ViewSerializer(serializers.Serializer):                # 它序列化的方式很类似于Django的forms
    id = serializers.IntegerField(read_only=True)
    country_id = serializers.IntegerField(default=-1)
    city_id = serializers.IntegerField(default=-1)
    name = serializers.CharField(max_length=200, default="")
    addr = serializers.CharField(max_length=200, default="")
    price = serializers.CharField(max_length=200, default="")
    lng = serializers.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    lat = serializers.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    pts = serializers.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    cmt_num = serializers.IntegerField(default=-1)
    tel = serializers.CharField(max_length=200,default="")
    time_cost = serializers.CharField(max_length=200, default="")
    trans = serializers.CharField(max_length=250, default="")
    open_time = serializers.CharField(max_length=200, default="")
    main_pic = serializers.CharField(max_length=200, default="")
    url = serializers.CharField(max_length=200,default="")
    status = serializers.IntegerField(default=-1)
    created = serializers.DateTimeField(default="")
    updated = serializers.DateTimeField(default="")

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.created = validated_data.get('created', instance.created)
        instance.upadted = validated_data.get('updated', instance.updated)
        instance.save()
        return instance

class HotelSerializer(serializers.Serializer):                # 它序列化的方式很类似于Django的forms
    id = serializers.IntegerField(read_only=True)
    country_id = serializers.IntegerField(default=-1)
    city_id = serializers.IntegerField(default=-1)
    name = serializers.CharField(max_length=200, default="")
    en_name = serializers.CharField(max_length=200, default="")
    addr = serializers.CharField(max_length=200, default="")
    price = serializers.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    lng = serializers.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    lat = serializers.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    cmt_num = serializers.IntegerField(default=-1)
    pts = serializers.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    pts_level = serializers.CharField(max_length=200,default="")
    note_num = serializers.IntegerField(default=-1)
    desc = serializers.CharField(max_length=200, default="")
    main_pic = serializers.CharField(max_length=200, default="")
    url = serializers.CharField(max_length=200,default="")
    status = serializers.IntegerField(default=-1)
    created = serializers.DateTimeField(default="")
    updated = serializers.DateTimeField(default="")

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.created = validated_data.get('created', instance.created)
        instance.upadted = validated_data.get('updated', instance.updated)
        instance.save()
        return instance


class EatSerializer(serializers.Serializer):                # 它序列化的方式很类似于Django的forms
    id = serializers.IntegerField(read_only=True)
    country_id = serializers.IntegerField(default=-1)
    city_id = serializers.IntegerField(default=-1)
    listrict_id = serializers.IntegerField(default=-1)
    name = serializers.CharField(max_length=200, default="")
    addr = serializers.CharField(max_length=200, default="")
    price = serializers.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    lng = serializers.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    lat = serializers.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    cmt_num = serializers.IntegerField(default=-1)
    pts = serializers.DecimalField(max_digits=16, decimal_places=8,default=0.0)
    pts_level = serializers.CharField(max_length=200, default="")
    tel = serializers.CharField(max_length=200, default="")
    dishes = serializers.CharField(max_length=200, default="")
    trans = serializers.CharField(max_length=200, default="")
    open_time = serializers.CharField(max_length=200, default="")
    main_pic = serializers.CharField(max_length=200,default="")
    url = serializers.CharField(max_length=200,default="")
    status = serializers.IntegerField(default=-1)
    created = serializers.DateTimeField(default="")
    updated = serializers.DateTimeField(default="")

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.created = validated_data.get('created', instance.created)
        instance.upadted = validated_data.get('updated', instance.updated)
        instance.save()
        return instance
