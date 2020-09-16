from django.shortcuts import render
from requests import Response
from rest_framework import generics, permissions
from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework.decorators import api_view

from pizzas.models import Pizza
from votes.models import Vote
from .serializers import PizzaSerializer, VoteSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly, ReadOnly


class PizzaList(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (ReadOnly,)
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
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
