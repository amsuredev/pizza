from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.TextField(max_length=50)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    @staticmethod
    def exist_pizza(id_pizza):
        for pizza in Pizza.objects.all():
            if pizza.id == id_pizza:
                return True
        return False
