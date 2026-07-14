from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'menu-items', MenuViewSet, basename='menu-items')
router.register(r'bookings', BookingViewSet, basename='bookings')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
