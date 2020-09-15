from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.
from .models import Vote
from pizzas.models import Pizza


class VoteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #create test user
        test_user1 = User.objects.create(
            username='test_user1',
            password="test_user1_password"
        )
        test_user1.save()
        #create test_pizza
        test_pizza1 = Pizza.objects.create(
            name="test_pizza1",
            price="7"
        )
        test_pizza1.save()
        #create vote
        test_vote = Vote.objects.create(author=test_user1, pizza=test_pizza1, vote_mark=4)
        test_vote.save()

    def test_vote_content(self):
        vote = Vote.objects.get(id=1)
        self.assertEqual(f'{vote.author}', 'test_user1')
        self.assertEqual(f'{vote.pizza}', 'test_pizza1')
        self.assertEqual(vote.vote_mark, 4)
'''
    def test_get_datas(self):
        list_users = []
        for vote in Vote.objects.all():
            list_users.append(vote.author)
        print(list_users)
'''