from django.urls import path
from .views import MenuItemListCreateView, BookingListCreateView

urlpatterns = [
    path('menu-items/', MenuItemListCreateView.as_view(), name='menu-items'),
    path('bookings/', BookingListCreateView.as_view(), name='bookings'),
]
