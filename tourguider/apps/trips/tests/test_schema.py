from unittest import skip

from django.contrib.contenttypes.models import ContentType
from snapshottest.django import TestCase
from graphene.test import Client

from tourguider.schema import public_schema
from .factories import TripFactory, PlaceFactory
from apps.reviews.tests.factories import ReviewFactory
from ..models import Trip

@skip('Aborting graphql implemenatation')
class TripSchemaTest(TestCase):
    def setUp(self):
        places = (PlaceFactory(name=place) for place in range(10))
        trip = TripFactory.create(places=places, name="Wycieczka po rynku")
        ReviewFactory.create(
            content_type=ContentType.objects.get_for_model(Trip), object_id=trip.id)
        self.client = Client(public_schema)

    def test_get_all_trips(self):
        schema = '''
            query{
              allTrips{
                name
                description
                places{
                  name
                }
              }
            }
        '''
        self.assertMatchSnapshot(self.client.execute(schema))

    def test_get_trip_with_reviews(self):
        schema = '''
        query{
          trip(id: 1){
            name
            description
            places{
              name
            }
            reviews{
              title
              rate
            }
          }
        }
        '''
        self.assertMatchSnapshot(self.client.execute(schema))

    def test_create_trip_with_places(self):
        schema = '''
        mutation{
          createTrip(name: "trip", description: "desc", places: [1,2,3]){
            trip{
              name
              places {
                name
              }
            }
          }
        }
        '''
        self.assertMatchSnapshot(self.client.execute(schema))

    def test_create_trip_properties(self):
        schema = '''
        mutation{
          createTrip(name: "trip", description: "desc", places: [1,2,3]){
            trip{
              name
              cost
              duration
              rate
              places {
                name
                rate
                duration
                cost
              }
            }
          }
        }
        '''
        self.assertMatchSnapshot(self.client.execute(schema))
