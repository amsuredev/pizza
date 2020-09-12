from django.urls import path

from .views import PizzaAPIView

urlpatterns = [
    path('', PizzaAPIView.as_view())
]