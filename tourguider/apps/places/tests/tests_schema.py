# from django.test import TestCase
from django.contrib.auth.models import User
from snapshottest.django import TestCase

from apps.places.models import Place
from .factories import PlaceFactory
from graphene.test import Client
from tourguider.schema import public_schema
from unittest import skip


@skip('Aborting graphql implemenatation')
class PlaceSchemaTest(TestCase):
    def setUp(self):
        PlaceFactory(name="Place")
        self.client = Client(public_schema)

    def test_all_places(self):
        executed = self.client.execute('''{ allPlaces{name description duration cost latitude }}''')
        assert executed == {
            'data': {
                'allPlaces': [
                    {
                        "name": "Place",
                        "description": "description",
                        "duration": "0:30:00",
                        "cost": 15.5,
                        "latitude": '51.10922092338914'
                    }
                ]
            }
        }

    def test_place(self):
        executed = self.client.execute('''{ place(id: 1){name}}''')
        assert executed == {
            'data': {
                "place": {
                    "name": "Place"
                }
            }
        }

    def test_create_place_without_guide(self):
        schema = '''
        mutation{
          createPlace(newPlace: {
            name: "New Place",
            description: "Awesome Place",
            duration: 50,
            cost: 5,
            city: "Wrocław"
          }){
            ok
            place{
              id
              name
              duration
            }
          }
        }
        '''
        self.assertMatchSnapshot(self.client.execute(schema))

    def test_create_place_with_guide(self):
        schema = '''mutation{
            createPlace(placeData: {name: "NewPlace",
                        description: "description",
                        duration: 5, city: "Wrocław",
                        address: "Plac", cost: 15},
              guideData: {name: "Guide", text: "guidetext", duration: 10, audioURL: "www.example.com"}){
                place{
                  name
                  description
                  duration
                  city
                  cost
                  guides{
                    duration
                    text
                    name
                    place {
                      name
                    }
                  }
                }
              }
            }'''
        self.assertMatchSnapshot(self.client.execute(schema))

    def test_edit_place(self):
        schema = '''
        mutation {
          editPlace(newPlace: {id: 1, name: "Edited name 2"}) {
            ok
            place{
              name
              id
            }
          }
        }

        '''
        self.assertMatchSnapshot(self.client.execute(schema))

    def test_delete_place(self):
        schema = '''
        mutation {
          deletePlace(id: 1){
            ok
            place{
              name
            }
          }
        }
        '''
        amount_places = len(Place.objects.all())
        self.assertMatchSnapshot(
            self.client.execute(schema, context_value={'user': User(id='1', username='Syrus')})
        )
        new_amount = len(Place.objects.all())
        self.assertEqual(amount_places-1, new_amount)
