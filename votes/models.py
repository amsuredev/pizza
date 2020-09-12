from django.db import models
# Create your models here.


#it is better to limit
class Vote(models.Model):
    id_user = models.PositiveIntegerField()
    id_pizza = models.PositiveIntegerField()
    vote_mark = models.PositiveIntegerField()
