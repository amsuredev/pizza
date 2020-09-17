from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pizza(models.Model):
    name = models.TextField(max_length=50)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @staticmethod
    def exist_pizza_by_id(id_pizza):
        for pizza in Pizza.objects.all():
            if pizza.id == id_pizza:
                return True
        return False

    @staticmethod
    def exist_such_pizza_name(name):
        for pizza in Pizza.objects.all():
            if pizza.name.__eq__(name):
                return True
        return False

    def save(self, *args, **kwargs):
        if not self.exist_such_pizza_name(self.name):
            super(Pizza, self).save(*args, **kwargs)
