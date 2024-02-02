# Inside Apps/tests.py
from django.test import TestCase
from datetime import datetime
from Apps.models import Reservation 

class ReservationModelTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.reservation = Reservation.objects.create(
            first_name='john',
            last_name='McDonald'
        )

    def test_fields(self):
        self.assertIsInstance(self.reservation.first_name, str)
        self.assertIsInstance(self.reservation.last_name, str)

    def test_timestamps(self):
        self.assertIsInstance(self.reservation.booking_time, datetime)
