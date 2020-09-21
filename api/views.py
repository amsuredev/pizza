from django.shortcuts import render
from requests import Response
from rest_framework import generics, permissions
from rest_framework import serializers


from django.contrib.auth.models import User
from rest_framework.decorators import api_view

from .serializers import PizzaSerializer, VoteSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly, ReadOnly
from .serializers import PizzaSerializer, VoteSerializer, UserSerializer,\
    ToppingSerializer, ToppingsInPizzaSerializer
from .permissions import IsAuthorOrReadOnly

from .models import Pizza, Topping, ToppingsInPizza, Vote


class PizzaList(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class VoteList(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ToppingList(generics.ListCreateAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class ToppingsInPizzaList(generics.ListAPIView):
    queryset = ToppingsInPizza.objects.all()
    serializer_class = ToppingsInPizzaSerializer

