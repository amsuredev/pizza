from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.TextField(max_length=50)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
