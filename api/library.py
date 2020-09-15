from pizzas.models import Pizza
from votes.models import Vote
import json
from django.http import HttpResponse


def get_res_of_voting(request):
    res_of_voting = {}
    for pizza in Pizza.objects.all():
        res_of_voting[pizza.name] = 0
    for vote in Vote.objects.all():
        res_of_voting[vote.pizza.name] += 1

    #for pizza in Pizza.objects.all():
    #    res_of_voting[pizza.name] = 0
    #    for vote in Vote.objects.all():
    #        if pizza.id == vote.pizza.id:
    #           res_of_voting[pizza.name] += 1
    #for vote in Vote.objects.all():
        #pizza_id = vote.pizza
        #pizza_obj = Pizza.objects.all().get(id=pizza_id)
        #pizza_name = pizza_obj.name
        #res_of_voting[pizza_name] += 1
        #res_of_voting[Pizza.objects.get(pk=vote.pizza).name] = res_of_voting[Pizza.objects.get(pk=vote.pizza).name] + 1
        #res_of_voting[vote.pizza] += 1
    return HttpResponse(json.dumps(res_of_voting))


