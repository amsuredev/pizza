from django.urls import path, include
from .library import get_res_of_voting
from .views import PizzaList, PizzaDetail, VoteList, VoteDetail, UserList

urlpatterns = [
    path('pizzas/', PizzaList.as_view()),
    path('pizzas/<int:pk>/', PizzaDetail.as_view()),
    path('votes/', VoteList.as_view()),
    path('votes/<int:pk>', VoteDetail.as_view()),
    path('voting_res/', get_res_of_voting),
    path('users/', UserList.as_view()),
    path('auth/', include('dj_rest_auth.urls')),#/auth/login/
    path('register/', include('dj_rest_auth.registration.urls'))
]