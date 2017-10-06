from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from snapshottest.django import TestCase
from graphene.test import Client

from apps.trips.models import Trip
from apps.trips.tests.factories import TripFactory, PlaceFactory
from tourguider.schema import public_schema
from .factories import ReviewFactory
from apps.reviews.tests.factories import ReviewFactory


class FakeAuth:
    def __init__(self, user):
        self.user = User.objects.create(
            username=user, email=f"{user}@gmail.com")


class TripSchemaTest(TestCase):
    def setUp(self):
        trip = TripFactory.create()
        place = PlaceFactory.create()
        ReviewFactory.create(
            content_type=ContentType.objects.get_for_model(Trip), object_id=trip.id)
        user = User.objects.create_user(
            username='TestUser', password='12345678')
        self.client = Client(public_schema)

    def test_get_all_reviews(self):
        schema = '''
        query{
          allReviews{
            title
            content
            rate
          }
        }
        '''
        self.assertMatchSnapshot(self.client.execute(schema))

    def test_get_one_review(self):
        schema = '''
        query{
          review(id: 1){
            title
            content
            rate
          }
        }
        '''
        self.assertMatchSnapshot(self.client.execute(schema))

    def test_create_trip_review(self):
        schema = '''
        mutation{
          createTripReview(reviewData: {content: "good", rate: 5, objectId: 1}){
            trip{
              name
            }
            review{
              content
              user {
                id
                username
              }
            }
          }
        }
        '''
        self.assertMatchSnapshot(self.client.execute(schema, context_value=FakeAuth('Peter')))

    def test_create_place_review(self):
        schema = '''
        mutation{
          createPlaceReview(reviewData: {content: "good", rate: 5, objectId: 1}){
            place{
              name
            }
            review{
              content
              user {
                id
                username
              }
            }
          }
        }
        '''
        self.assertMatchSnapshot(self.client.execute(schema, context_value=FakeAuth('Peter')))
