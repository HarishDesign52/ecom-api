from django.urls import path
from django.views.generic import RedirectView

from .views import OrderView

urlpatterns = [
    path('orders/', OrderView.as_view(), name="order"),
    path("", RedirectView.as_view(url="orders/"))
]
