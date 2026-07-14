from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


def index(request):
    """Serves the static home page for Little Lemon."""
    return render(request, 'index.html')


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
