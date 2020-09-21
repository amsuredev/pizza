from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Pizza, Vote, ToppingsInPizza, Topping

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'name', 'price', 'author')


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('id', 'author', 'pizza')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('id', 'name')


class ToppingsInPizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToppingsInPizza
        fields = ('pizza', 'topping')


