from .views import MenuItemsView, SingleMenuItemView, home
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', home, name="home"),
    path('reservation/menu-items/', MenuItemsView.as_view()),
    path('reservation/menu-item<int:pk>/', SingleMenuItemView.as_view()),
    path('reservation/api-token-auth/', obtain_auth_token),
]