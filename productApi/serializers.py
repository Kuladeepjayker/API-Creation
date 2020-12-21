from rest_framework import serializers
from .models import Signup, Login, Plant, Order


class SignupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Signup
        fields = ('name', 'email', 'password')


class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Login
        fields = ('name', 'password')


class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ('category', 'plant')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('name', 'order')


