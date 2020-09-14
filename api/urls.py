from django.urls import path

from .views import PizzaList, PizzaDetail, VoteList, VoteDetail

urlpatterns = [
    path('pizzas/', PizzaList.as_view()),
    path('pizzas/<int:pk>/', PizzaDetail.as_view()),
    path('votes/', VoteList.as_view()),
    path('votes/<int:pk>', VoteDetail.as_view())
]