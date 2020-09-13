from django.db import models
# Create your models here.
from django.contrib.auth.models import User


#it is better to limit
class Vote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    id_pizza = models.PositiveIntegerField()
    vote_mark = models.PositiveIntegerField()
