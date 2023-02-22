from .views import MenuItemsView, SingleMenuItemView
from django.urls import path

urlpatterns = [
    path('items/', MenuItemsView.as_view()),
    path('item/<int:pk>', SingleMenuItemView.as_view()),
]