from django.test import TestCase
from restaurant.models import Menu, Booking
from django.utils import timezone


class MenuModelTest(TestCase):
    def test_create_menu_item(self):
        item = Menu.objects.create(title="Greek Salad", price=12.50, inventory=100)
        self.assertEqual(str(item), "Greek Salad")
        self.assertEqual(item.price, 12.50)
        self.assertEqual(item.inventory, 100)


class BookingModelTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=timezone.now(),
        )
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guests, 4)
