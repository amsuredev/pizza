from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import permissions

from pizzas.models import Pizza
from votes.models import Vote
import json
from django.http import HttpResponse
from django.contrib.auth.models import User

@api_view(['GET'])
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
        id_user = int(request.data['id_user'])
        id_pizza = int(request.data['id_pizza'])
    except:
        return HttpResponse(json.dumps({'status': 'Incorrect data type'}))
    if request.user.id == id_user and Pizza.exist_pizza(id_pizza) and first_vote(request.user.id):
        Vote(pizza_id=id_pizza, author_id=id_user).save()
    return HttpResponse(json.dumps({'status': 'Correct data types'}))


def first_vote(author_id):
    for vote in Vote.objects.all():
        if vote.author_id == author_id:
            return False
    return True
