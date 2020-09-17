from django.db import models

# Create your models here.


class Topping(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.exist_topping(self.name):
            super(Topping, self).save(*args, **kwargs)

    @staticmethod
    def exist_topping(name):
        for topping in Topping.objects.all():
            if topping.name.__eq__(name):
                return True
        return False
