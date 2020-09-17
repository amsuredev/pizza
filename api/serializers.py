from rest_framework import serializers
from pizzas.models import Pizza
from votes.models import Vote
from django.contrib.auth.models import User
from toppings.models import Topping
from toppings_in_pizza.models import ToppingsInPizza


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'name', 'price')


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


