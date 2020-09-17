from django.urls import path, include
from .views_functions import get_res_of_voting, post_vote, amount_of_toppings, add_toppings_in_pizza, add_pizza
from .views import PizzaList, PizzaDetail, VoteList, VoteDetail, UserList, ToppingList, ToppingsInPizzaList

urlpatterns = [
    path('pizzas/', PizzaList.as_view()),
    path('add_pizza/', add_pizza),
    path('pizzas/<int:pk>/', PizzaDetail.as_view()),
    path('votes/', VoteList.as_view()),
    path('post_vote/', post_vote),
    path('votes/<int:pk>', VoteDetail.as_view()),
    path('voting_res/', get_res_of_voting),
    path('users/', UserList.as_view()),
    path('auth/', include('dj_rest_auth.urls')),#/auth/login/
    path('register/', include('dj_rest_auth.registration.urls')),
    path('toppings/', ToppingList.as_view()),
    path('amount_of_toppings/', amount_of_toppings),
    path('toppings_in_pizza/', ToppingsInPizzaList.as_view()),
    path('add_toppings_in_pizza/', add_toppings_in_pizza),
]
