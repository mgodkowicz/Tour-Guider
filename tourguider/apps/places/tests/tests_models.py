from django.test import TestCase

from .factories import PlaceFactory


class PlaceModelTest(TestCase):
    def test_create_model(self):
        place = PlaceFactory()
        self.assertEqual(place.name, "Place 000")
        self.assertEqual(place.latitude, 51.10922092338914)

