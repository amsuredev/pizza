from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers


from pizzas.models import Pizza
from votes.models import Vote
from .serializers import PizzaSerializer, VoteSerializer


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
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
