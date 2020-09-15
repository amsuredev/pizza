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
            price=7
        )
        test_pizza1.save()
        #create vote
        test_vote = Vote.objects.create(author=test_user1, pizza=test_pizza1)
        test_vote.save()

        #add second same vote
        test_vote_same = Vote.objects.create(author=test_user1, pizza=test_pizza1)
        test_vote_same.save()

    def test_vote_content(self):
        vote = Vote.objects.get(id=1)
        self.assertEqual(f'{vote.author}', 'test_user1')
        self.assertEqual(f'{vote.pizza}', 'test_pizza1')

    @staticmethod
    def exist_repeats(check_vote: Vote):
        for vote in Vote.objects.all():
            if vote.pizza.__eq__(check_vote.pizza) and vote.author.__eq__(check_vote.pizza):
                return True
        return False

    def test_similar_vote_repeat(self):
        for vote in Vote.objects.all():
            self.assertEqual(self.exist_repeats(vote), False)


