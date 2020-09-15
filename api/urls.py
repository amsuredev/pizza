from django.urls import path
from .library import get_res_of_voting
from .views import PizzaList, PizzaDetail, VoteList, VoteDetail

urlpatterns = [
    path('pizzas/', PizzaList.as_view()),
    path('pizzas/<int:pk>/', PizzaDetail.as_view()),
    path('votes/', VoteList.as_view()),
    path('votes/<int:pk>', VoteDetail.as_view()),
    path('test', get_res_of_voting)
]