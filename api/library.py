from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import permissions

from pizzas.models import Pizza
from votes.models import Vote
import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from toppings_in_pizza.models import ToppingsInPizza
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
    if Pizza.exist_pizza(id_pizza):
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
