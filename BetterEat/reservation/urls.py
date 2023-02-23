from .views import MenuItemsView, SingleMenuItemView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('items/', MenuItemsView.as_view()),
    path('item<int:pk>/', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]