from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pizza(models.Model):
    name = models.TextField(max_length=50, unique=True)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


