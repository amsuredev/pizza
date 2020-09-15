from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from pizzas.models import Pizza


#it is better to limit
class Vote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return 'author: ' + str(self.author.id) + ' pizza: ' + str(self.pizza.id)

    # not allow to add same votes
    def save(self, *args, **kwargs):
        if not exist_vote(self.author, self.pizza):
            super(Vote, self).save(*args, **kwargs)


def exist_vote(author, pizza):
    for vote in Vote.objects.all():
        if vote.author.__eq__(author) and vote.pizza.__eq__(pizza):
            return True
    return False
