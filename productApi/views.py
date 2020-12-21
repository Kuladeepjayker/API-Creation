from rest_framework import viewsets
from .serializers import SignupSerializer, LoginSerializer, PlantSerializer, OrderSerializer
from .models import Signup, Login, Plant, Order


class SignupViewSet(viewsets.ModelViewSet):
    queryset = Signup.objects.all().order_by('name')
    serializer_class = SignupSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all().order_by('name')
    serializer_class = LoginSerializer


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all().order_by('category')
    serializer_class = PlantSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('name')
    serializer_class = OrderSerializer