from django.shortcuts import render
from requests import Response
from rest_framework import generics, permissions, response, status
from rest_framework import serializers
from toppings.models import Topping
from toppings_in_pizza.models import ToppingsInPizza

from django.contrib.auth.models import User
from rest_framework.decorators import api_view

from pizzas.models import Pizza
from votes.models import Vote
from .serializers import PizzaSerializer, VoteSerializer, UserSerializer,\
    ToppingSerializer, ToppingsInPizzaSerializer
from .permissions import IsAuthorOrReadOnly


class PizzaList(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class VoteList(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    #def post(self, request, *args, **kwargs):
        #if request.user.pk == self.serializer_class.Meta.model.author:
        #super(VoteList, self).post(self, request)
        #super(VoteList, self).post(self, request, *args, **kwargs)


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ToppingList(generics.ListCreateAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class ToppingsInPizzaList(generics.ListCreateAPIView):
    queryset = ToppingsInPizza.objects.all()
    serializer_class = ToppingsInPizzaSerializer
#@api_view(['POST'])
#def post_vote(request):
