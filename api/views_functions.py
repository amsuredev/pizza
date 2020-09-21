from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import permissions

from pizzas.models import Pizza
from votes.models import Vote
import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from toppings_in_pizza.models import ToppingsInPizza
from toppings.models import Topping
from .permissions import ReadOnly



@api_view(['GET'])
@permission_classes((ReadOnly,))
def get_res_of_voting(request):
    res_of_voting = {}
    for pizza in Pizza.objects.all():
        res_of_voting[pizza.name] = 0
    for vote in Vote.objects.all():
        res_of_voting[vote.pizza.name] += 1
    return HttpResponse(json.dumps(res_of_voting))


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def post_vote(request):
    try:
        id_pizza = int(request.data['id_pizza'])
    except:
        return HttpResponse(json.dumps({'status': 'Incorrect data type'}))
    if Pizza.objects.filter(pk=id_pizza).exists() and Vote.objects.filter(author_id=request.user.id).exists():
        Vote(pizza_id=id_pizza, author_id=request.user.id).save()
    if Pizza.filter(pk=id_pizza):
        Vote(author=request.user, pizza_id=id_pizza).save()
    return HttpResponse(json.dumps({'status': 'Correct data types'}))


@api_view(['GET'])
def amount_of_toppings(request):
    amount_top = {}
    for pizza in Pizza.objects.all():
        amount_top[pizza.name] = 0
    for topping in ToppingsInPizza.objects.all():
        amount_top[topping.pizza.name] += 1
    return HttpResponse(json.dumps(amount_top))


@api_view(['POST'])
def add_toppings_in_pizza(request):
    try:
        id_pizza = int(request.data['id_pizza'])
        id_topping = int(request.data['id_topping'])
    except:
        return HttpResponse(json.dumps({'status': 'Incorrect data type'}))

    if Pizza.objects.filter(pk=id_pizza) and Topping.objects.filter(pk=id_topping):
        if Pizza.objects.get(id=id_pizza).author.id.__eq__(request.user.id):
            ToppingsInPizza(pizza_id=id_pizza, topping_id=id_topping).save()
            return HttpResponse(json.dumps({'status': 'Save if not existed'}))
    return HttpResponse(json.dumps({'status': 'Not existed pizza or topping id or not pizza author'}))


@api_view(['POST'])
def add_pizza(request):
    try:
        pizza_name = str(request.data['pizza_name'])
        pizza_price = int(request.data['pizza_price'])
    except:
        return HttpResponse(json.dumps({'status': 'Incorrect data type'}))
    Pizza(name=pizza_name, price=pizza_price, author=request.user).save()
    return HttpResponse(json.dumps({'status': 'Correct data type'}))
