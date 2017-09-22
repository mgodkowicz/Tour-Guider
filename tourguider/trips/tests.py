from django.test import TestCase
from django.utils.timezone import timedelta
from factory import Sequence, SubFactory, post_generation
from factory.django import DjangoModelFactory, ImageField

from .models import Trip
from places.tests import PlaceFactory


class TripFactory(DjangoModelFactory):
    class Meta:
        model = Trip

    name = Sequence(lambda n: "Trip %03d" % n)
    description = "description"
    rate = 5
    places = SubFactory(PlaceFactory)

    @post_generation
    def places(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for place in extracted:
                self.places.add(place)


class TripModelTest(TestCase):
    def test_create_model(self):
        trip = TripFactory()
        self.assertEqual("Trip 000", trip.name)

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

