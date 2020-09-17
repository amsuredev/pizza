from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pizza(models.Model):
    name = models.TextField(max_length=50)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #toppings = CollectionField()

    def __str__(self):
        return self.name

    @staticmethod
    def exist_pizza(id_pizza):
        for pizza in Pizza.objects.all():
            if pizza.id == id_pizza:
                return True
        return False
