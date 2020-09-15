from django.test import TestCase
from .models import Pizza

# Create your tests here.


class VoteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_pizza1 = Pizza.objects.create(name='test_pizza', price=3)
        test_pizza1.save()

    def test_pizza_content(self):
        test_pizza1 = Pizza.objects.get(pk=1)
        self.assertEqual(test_pizza1.name, 'test_pizza')
        self.assertEqual(test_pizza1.price, 3)