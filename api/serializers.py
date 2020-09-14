from rest_framework import serializers
from pizzas.models import Pizza
from votes.models import Vote


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('name', 'price')


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('author', 'pizza')


