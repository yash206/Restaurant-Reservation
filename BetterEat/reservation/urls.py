from .views import MenuItemsView, SingleMenuItemView, msg
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', MenuItemsView.as_view()),
    path('menu-item<int:pk>/', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('message/', msg),
]