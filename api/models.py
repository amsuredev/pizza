from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Pizza(models.Model):
    name = models.TextField(max_length=50, unique=True)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_pizza')

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class ToppingsInPizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)

    def __str__(self):
        return self.pizza.name + ' ' + self.topping.name

    def save(self, *args, **kwargs):
        if not ToppingsInPizza.objects.filter(pizza_name=self.pizza_name, topping_name=self.topping_name).exists():
            super(ToppingsInPizza, self).save(*args, **kwargs)


class Vote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_vote')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return 'author: ' + str(self.author.id) + ' pizza: ' + str(self.pizza.id)

    # not allow to vote two or more times
    def save(self, *args, **kwargs):
        if not Vote.objects.filter(author_id=self.author.id).exists():
            super(Vote, self).save(*args, **kwargs)