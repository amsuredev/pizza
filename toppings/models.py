from django.db import models

# Create your models here.


class Topping(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.exist_topping_name(self.name):
            super(Topping, self).save(*args, **kwargs)

    @staticmethod
    def exist_topping(id_topping):#for adding ToppingsInPizza
        for topping in Topping.objects.all():
            if topping.id.__eq__(id_topping):
                return True
        return False

    @staticmethod
    def exist_topping_name(name):
        for topping in Topping.objects.all():
            if topping.objects.name__eq__(name):
                return True
        return False
