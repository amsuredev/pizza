from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from pizzas.models import Pizza
from .serializers import PizzaSerializer

class PizzaAPIView(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer