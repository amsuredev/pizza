from django.shortcuts import render
from requests import Response
from rest_framework import generics, permissions
from rest_framework import serializers
<<<<<<< HEAD
=======
from toppings.models import Topping
from toppings_in_pizza.models import ToppingsInPizza
>>>>>>> update

from django.contrib.auth.models import User
from rest_framework.decorators import api_view

from pizzas.models import Pizza
from votes.models import Vote
<<<<<<< HEAD
from .serializers import PizzaSerializer, VoteSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly, ReadOnly
=======
from .serializers import PizzaSerializer, VoteSerializer, UserSerializer,\
    ToppingSerializer, ToppingsInPizzaSerializer
from .permissions import IsAuthorOrReadOnly
>>>>>>> update


class PizzaList(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
<<<<<<< HEAD
    permission_classes = (ReadOnly,)
=======
    permission_classes = (IsAuthorOrReadOnly,)
>>>>>>> update
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
<<<<<<< HEAD
=======


class ToppingList(generics.ListCreateAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class ToppingsInPizzaList(generics.ListAPIView):
    queryset = ToppingsInPizza.objects.all()
    serializer_class = ToppingsInPizzaSerializer
>>>>>>> update
