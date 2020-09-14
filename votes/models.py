from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from pizzas.models import Pizza


#it is better to limit
class Vote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)