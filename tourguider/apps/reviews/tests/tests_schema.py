from django.contrib.contenttypes.models import ContentType
from snapshottest.django import TestCase
from graphene.test import Client

from tourguider.schema import public_schema
from .factories import ReviewFactory
from apps.reviews.tests.factories import ReviewFactory


# class TripSchemaTest(TestCase):
#     def setUp(self):
#         places = (PlaceFactory(name=place) for place in range(10))
#         trip = TripFactory.create(places=places)
#         ReviewFactory.create(
#             content_type=ContentType.objects.get_for_model(Trip), object_id=trip.id)
#         self.client = Client(public_schema)
