from django.db import models
from pizzas.models import Pizza
from toppings.models import Topping
from django.contrib.auth.models import User
# Create your models here.


class ToppingsInPizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)

    def __str__(self):
        return self.pizza.name + ' ' + self.topping.name

    def save(self, *args, **kwargs):
        if not ToppingsInPizza.objects.filter(pizza_name=self.pizza_name, topping_name=self.topping_name).exists():
            super(ToppingsInPizza, self).save(*args, **kwargs)
