from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.places.api.serializers import PlaceSerializer, PlaceDetailSerializer, OpeningHourSerializer
from apps.places.models import Place, OpeningHour
from apps.places.tests.factories import PlaceFactory, HourFactory
from apps.trips.models import Trip
from apps.trips.tests.factories import TripFactory


class GetAllPlacesTest(APITestCase):
    def setUp(self):
        PlaceFactory.create(name="Place1")
        PlaceFactory.create(name="Place2")
        PlaceFactory.create(name="Place3")

    def test_get_all_places(self):
        response = self.client.get(reverse('api-place:list'))
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePlaceTest(APITestCase):
    def setUp(self):
        self.place = PlaceFactory.create()

    def test_get_valid_single_place(self):
        response = self.client.get(
            reverse('api-place:detail', kwargs={'pk': self.place.id}))
        trip = Place.objects.first()
        serializer = PlaceDetailSerializer(trip)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_place(self):
        response = self.client.get(
            reverse('api-place:detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPlaceTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="nerd")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.valid_payload = {
            'name': 'New place',
            'description': 'Best place!',
            'duration': '00:30:00'
        }
        self.invalid_payload = {
            'name': '',
            'description': 'Best place!'
        }

    def test_create_valid_place_by_admin(self):
        self.user.is_staff = True
        response = self.client.post(
            reverse('api-place:list'),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_place_by_admin(self):
        self.user.is_staff = True
        response = self.client.post(
            reverse('api-place:list'),
            data=self.invalid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_place_by_user(self):
        """Regular user can not create new places"""
        self.user.is_staff = False
        response = self.client.post(
            reverse('api-place:list'),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UpdateSinglePlaceTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="nerd")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        PlaceFactory.create()
        PlaceFactory.create()
        self.valid_payload = {
            'name': 'New place',
            'description': 'Best place!',
            'duration': '00:30:00'
        }
        self.invalid_payload = {
            'name': 'WrongName',
            'description': '',
        }

    def test_valid_update_place(self):
        self.user.is_staff = True
        response = self.client.put(
            reverse('api-place:detail', kwargs={'pk': 1}),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_place(self):
        self.user.is_staff = True
        response = self.client.put(
            reverse('api-place:detail', kwargs={'pk': 1}),
            data=self.invalid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_regular_user_cant_update_place(self):
        self.user.is_staff = False
        response = self.client.put(
            reverse('api-place:detail', kwargs={'pk': 1}),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class DeleteSinglePlaceTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="nerd", is_staff=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.place_1 = PlaceFactory.create()
        self.place_2 = PlaceFactory.create()

    def test_valid_delete_place(self):
        response = self.client.delete(
            reverse('api-place:detail', kwargs={'pk': self.place_2.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_place(self):
        response = self.client.delete(
            reverse('api-place:detail', kwargs={'pk': 100}),
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_regular_user_cant_delete_place(self):
        self.user.is_staff = False
        response = self.client.delete(
            reverse('api-place:detail', kwargs={'pk': self.place_2.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class GetPlacesForOneTripTest(APITestCase):
    def setUp(self):
        places = (PlaceFactory(name=place) for place in range(2))
        self.trip = TripFactory.create(places=places, name="Wycieczka po rynku")

    def test_get_all_places(self):
        response = self.client.get(
            reverse('api-trip:places-list',
                    kwargs={'trip_pk': self.trip.id}
                    )
        )
        trip = Trip.objects.get(id=self.trip.id)
        serializer = PlaceSerializer(trip.places, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetPlaceOpeningHoursTest(APITestCase):
    def setUp(self):
        self.hours = (HourFactory() for _ in range(5))
        self.place = PlaceFactory()
        self.place.hours.add(*list(self.hours))

    def test_get_all_hours(self):
        response = self.client.get(
            reverse('api-place:hours', kwargs={'pk': self.place.id})
        )
        hours = OpeningHour.objects.all()
        serializer = OpeningHourSerializer(hours, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreatePlaceOpeningHourTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="nerd", is_staff=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.place = PlaceFactory()

        self.valid_payload = {
            'weekday': 1,
            'opening_hour': '08:30:00',
            'closing_hour': '16:30:00'
        }
        self.invalid_payload = {
            'weekday': 2,
            'closing_hour': '16:30:00'
        }

    def test_create_valid_hour_by_admin(self):
        self.user.is_staff = True
        response = self.client.post(
            reverse('api-place:hours', kwargs={'pk': self.place.id}),
            data=self.valid_payload
        )
        hour = OpeningHour.objects.get(id=response.data['id'])
        self.assertTrue(hour.place_set.filter(id=self.place.id).exists())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_hour_by_admin(self):
        response = self.client.post(
            reverse('api-place:hours', kwargs={'pk': self.place.id}),
            data=self.invalid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_hour_by_user(self):
        """Regular user can not create hours"""
        self.user.is_staff = False
        response = self.client.post(
            reverse('api-place:hours', kwargs={'pk': self.place.id}),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
