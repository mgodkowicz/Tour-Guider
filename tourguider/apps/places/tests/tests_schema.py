# from django.test import TestCase
from snapshottest.django import TestCase
from .factories import PlaceFactory
from graphene.test import Client
from tourguider.schema import public_schema


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
            createPlace(placeData: {name: "NewPlace",
                        description: "description",
                        duration: 5, city: "Wrocław",
                        address: "Plac", cost: 15}){
            place{
              name
              description
              duration
              city
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
