from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from reservation import views


router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('reservation.urls')),
    path('reservation/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
