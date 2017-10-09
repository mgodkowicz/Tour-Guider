import datetime

from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.places.api.serializers import PlaceSerializer, PlaceDetailSerializer, OpeningHourSerializer, GuideSerializer
from apps.places.models import Place, OpeningHour, Guide
from apps.places.tests.factories import PlaceFactory, HourFactory, GuideFactory
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
            reverse('api-place:detail', kwargs={'pk': 1000}))
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
            'closing_hour': '16:30:00'
        }
        self.valid_updated_payload = {
            'weekday': 1,
            'opening_hour': '08:00:00',
            'closing_hour': '16:00:00'
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

    def test_create_same_valid_hour(self):
        response = self.client.post(
            reverse('api-place:hours', kwargs={'pk': self.place.id}),
            data=self.valid_payload
        )
        hour = OpeningHour.objects.get(id=response.data['id'])
        self.assertEqual(hour.id, 1)

    def test_create_second_monday_hour(self):
        """When creating hour for existing day, object should update himself"""
        response = self.client.post(
            reverse('api-place:hours', kwargs={'pk': self.place.id}),
            data=self.valid_updated_payload
        )
        hour = OpeningHour.objects.get(id=response.data['id'])
        self.assertEqual(hour.id, 1)
        self.assertEqual(hour.opening_hour, datetime.time(8, 0))
        self.assertEqual(OpeningHour.objects.all().count(), 1)
        self.assertEqual(self.place.hours.first(), hour)


class GetPlaceGuidesTest(APITestCase):
    def setUp(self):
        self.place = PlaceFactory()
        self.guide = GuideFactory(place=self.place)
        self.guide_2 = GuideFactory(place=self.place)

    def test_get_all_guides(self):
        response = self.client.get(
            reverse('api-place:guides',
                    kwargs={'pk': self.place.id}
                    )
        )
        guides = Guide.objects.filter(place=self.place)
        serializer = GuideSerializer(guides, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_guides_for_invalid_place(self):
        response = self.client.get(
            reverse('api-place:guides',
                    kwargs={'pk': 100}
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewGuideTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="nerd", is_staff=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.place = PlaceFactory()
        self.valid_payload = {
            'name': 'Best Place Guide',
            'text': 'this is beautiful place',
            'audioURL': 'http://www.link.com',
            'duration': '00:10:00',
            'place': self.place.id
        }
        self.invalid_payload = {
            'text': 'this is wrong place',
            'audioURL': 'www.link.com',
            'duration': '00:10:00',
            'place': self.place.id
        }

    def test_create_valid_guide_by_admin(self):
        response = self.client.post(
            reverse('api-place:guides',
                    kwargs={'pk': self.place.id}),
            data=self.valid_payload
        )
        guide = Guide.objects.get(id=response.data['id'])
        self.assertTrue(guide.place == self.place)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_guide_by_admin(self):
        response = self.client.post(
            reverse('api-place:guides',
                    kwargs={'pk': self.place.id}),
            data=self.invalid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_guide_invalid_place(self):
        response = self.client.post(
            reverse('api-place:guides',
                    kwargs={'pk': 100}),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_guide_by_user(self):
        self.user.is_staff = False
        response = self.client.post(
            reverse('api-place:guides',
                    kwargs={'pk': self.place.id}),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class GetSinglePlaceGuideTest(APITestCase):
    def setUp(self):
        self.place = PlaceFactory()
        self.guide = GuideFactory(place=self.place)

    def test_get_valid_single_guide(self):
        response = self.client.get(
            reverse('api-place:guide-detail',
                    kwargs={'pk': self.place.id,
                            'guide_pk': self.guide.id}
                    )
        )
        guide = Guide.objects.first()
        serializer = GuideSerializer(guide)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_place_single_guide(self):
        response = self.client.get(
            reverse('api-place:guide-detail',
                    kwargs={'pk': 100,
                            'guide_pk': self.guide.id}
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_single_guide(self):
        response = self.client.get(
            reverse('api-place:guide-detail',
                    kwargs={'pk': self.place.id,
                            'guide_pk': 10}
                    )
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateSingleGuideTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="nerd", is_staff=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.place = PlaceFactory()
        self.guide = GuideFactory(place=self.place)
        self.valid_payload = {
            'name': 'Best Place Guide',
            'text': 'this is beautiful place',
            'audioURL': 'http://www.link.com',
            'duration': '00:10:00',
            'place': self.place.id
        }
        self.invalid_payload = {
            'text': 'this is wrong place',
            'audioURL': 'www.link.com',
            'duration': '00:10:00',
            'place': self.place.id
        }

    def test_valid_update_guide(self):
        response = self.client.put(
            reverse('api-place:guide-detail',
                    kwargs={'pk': self.place.id,
                            'guide_pk': self.guide.id}),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_guide(self):
        response = self.client.put(
            reverse('api-place:guide-detail',
                    kwargs={'pk': self.place.id,
                            'guide_pk': self.guide.id}),
            data=self.invalid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_regular_user_cant_update_guide(self):
        self.user.is_staff = False
        response = self.client.put(
            reverse('api-place:guide-detail',
                    kwargs={'pk': self.place.id,
                            'guide_pk': self.guide.id}),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class DeleteSingleGuideTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="nerd", is_staff=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.place = PlaceFactory()
        self.guide = GuideFactory(place=self.place)

    def test_valid_delete_guide(self):
        response = self.client.delete(
            reverse('api-place:guide-detail',
                    kwargs={'pk': self.place.id,
                            'guide_pk': self.guide.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_guide(self):
        response = self.client.delete(
            reverse('api-place:guide-detail',
                    kwargs={'pk': 100,
                            'guide_pk': self.guide.id})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_regular_user_cant_delete_guide(self):
        self.user.is_staff = False
        response = self.client.delete(
            reverse('api-place:guide-detail',
                    kwargs={'pk': self.place.id,
                            'guide_pk': self.guide.id})
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
