from .views import menuview, bookingview
from django.urls import path

urlpatterns = [
    path("menu/", menuview.as_view()),
    path("booking/", bookingview.as_view()),
]