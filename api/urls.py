from django.urls import path

from .views import PizzaList, PizzaDetail

urlpatterns = [
    path('pizzas/', PizzaList.as_view()),
    path('pizzas/<int:pk>/', PizzaDetail.as_view())
]