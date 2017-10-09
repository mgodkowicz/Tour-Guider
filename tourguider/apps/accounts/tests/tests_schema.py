from django.contrib.auth.models import User
from snapshottest.django import TestCase
from graphene.test import Client

from tourguider.schema import public_schema


class TripSchemaTest(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='TestUser', password='12345678')

        self.client = Client(public_schema)

    def test_create_user(self):
        schema = '''
        mutation{
            createUser(username: "TestUser2", password: "12345678", email: "m@m.com"){
            user{
              username
            }
          }
        }
        '''
        self.assertMatchSnapshot(self.client.execute(schema))

    def test_get_all_users(self):
        schema = '''
        query{
          allUsers{
            username
            id
          }
        }
        '''
        self.assertMatchSnapshot(self.client.execute(schema))

    def test_get_user(self):
        schema = '''
        query{
          user(id: 1){
            username
            id
          }
        }
        '''
        self.assertMatchSnapshot(self.client.execute(schema))

    def test_valid_login(self):
        schema = '''
        mutation{
            login(username: "TestUser", password: "12345678"){
            user{
              username
            }
          }
        }'''
        self.assertMatchSnapshot(self.client.execute(schema))
