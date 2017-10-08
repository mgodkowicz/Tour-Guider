from django.test import TestCase

from .factories import PlaceFactory, GuideFactory
from ..models import Place


class PlaceModelTest(TestCase):
    def test_create_model(self):
        place = PlaceFactory(name="Place 000")
        self.assertEqual(place.name, "Place 000")
        self.assertEqual(place.latitude, 51.10922092338914)

    def test_create_guide_model(self):
        guide = GuideFactory(name="Guide 000")
        self.assertEqual(guide.name, "Guide 000")
        self.assertEqual(type(guide.place), Place)
