from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
