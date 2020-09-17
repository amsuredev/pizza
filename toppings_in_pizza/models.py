from django.db import models
from pizzas.models import Pizza
from toppings.models import Topping
# Create your models here.


class ToppingsInPizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)

    def __str__(self):
        return self.pizza.name + ' ' + self.topping.name

    def save(self, *args, **kwargs):
        if not self.exist_topping_in_pizza(self.pizza.name, self.topping.name):
            super(ToppingsInPizza, self).save(*args, **kwargs)

    @staticmethod
    def exist_topping_in_pizza(pizza_name, topping_name):
        for topping_in_pizza in ToppingsInPizza.objects.all():
            if topping_in_pizza.pizza.name.__eq__(pizza_name) \
                    and topping_in_pizza.topping.name.__eq__(topping_in_pizza):
                return True
        return False
