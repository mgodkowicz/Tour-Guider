from django.test import TestCase
from django.utils.timezone import timedelta

from apps.places.tests.factories import PlaceFactory
from .factories import TripFactory


class TripModelTest(TestCase):
    def test_create_model(self):
        trip = TripFactory(name="Trip 001")
        self.assertEqual("Trip 001", trip.name)

    def test_trip_places_amount(self):
        places = (PlaceFactory() for _ in range(10))
        trip = TripFactory.create(places=places)
        self.assertEqual(10, len(trip.places.all()))

    def test_cost_and_duration(self):
        """Test calculating trip cost and duration base on places costs/duration"""
        duration = timedelta(minutes=10)
        places = (PlaceFactory(cost=10, duration=duration) for _ in range(10))
        trip = TripFactory.create(places=places)
        self.assertEqual(100.0, trip.cost)
        self.assertEqual(timedelta(minutes=100), trip.duration)

