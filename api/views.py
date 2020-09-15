from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import serializers


from django.contrib.auth.models import User
from pizzas.models import Pizza
from votes.models import Vote
from .serializers import PizzaSerializer, VoteSerializer, UserSerializer
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


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
