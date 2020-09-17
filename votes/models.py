from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from pizzas.models import Pizza


class Vote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return 'author: ' + str(self.author.id) + ' pizza: ' + str(self.pizza.id)

    # not allow to vote two or more times
    def save(self, *args, **kwargs):
        if self.first_vote(self.author.id):
            super(Vote, self).save(*args, **kwargs)

    @staticmethod
    def first_vote(author_id):
        for vote in Vote.objects.all():
            if author_id == vote.author_id:
                return False
        return True

