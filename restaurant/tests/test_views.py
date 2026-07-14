from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from restaurant.models import Menu, Booking


class MenuViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="testpass123")
        self.client.force_authenticate(user=self.user)
        self.menu_item = Menu.objects.create(title="Bruschetta", price=8.00, inventory=50)

    def test_get_menu_items(self):
        response = self.client.get('/api/menu-items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_menu_item(self):
        data = {"title": "Pasta", "price": "15.00", "inventory": 20}
        response = self.client.post('/api/menu-items/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class BookingViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester2", password="testpass123")
        self.client.force_authenticate(user=self.user)

    def test_create_booking(self):
        data = {
            "name": "Jane Smith",
            "no_of_guests": 2,
            "booking_date": timezone.now().isoformat(),
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_bookings(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
