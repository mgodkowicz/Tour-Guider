from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.places.tests.factories import PlaceFactory
from apps.reviews.api.serializers import ReviewSerializer
from apps.reviews.models import Review
from apps.reviews.tests.factories import ReviewFactory
from apps.trips.models import Trip
from apps.trips.tests.factories import TripFactory


class GetAllTripReviewsTest(APITestCase):
    def setUp(self):
        self.trip = TripFactory()
        self.trip2 = TripFactory()
        self.ct = ContentType.objects.get_for_model(self.trip)
        ReviewFactory.create(
            content_type=self.ct,
            object_id=self.trip.id)

    def test_get_all_reviews(self):
        response = self.client.get(reverse('api-trip:reviews',
                                   kwargs={'trip_pk': self.trip.id}))
        reviews = Review.objects.filter(content_type=self.ct,
                                        object_id=self.trip.id)
        serializer = ReviewSerializer(reviews, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_empty_reviews_list(self):
        response = self.client.get(reverse('api-trip:reviews',
                                   kwargs={'trip_pk': self.trip2.id}))
        reviews = Review.objects.filter(content_type=self.ct,
                                        object_id=self.trip2.id)
        serializer = ReviewSerializer(reviews, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(reviews), 0)


class GetAllPlaceReviewsTest(APITestCase):
    def setUp(self):
        self.place = PlaceFactory()
        self.place2 = PlaceFactory()
        self.ct = ContentType.objects.get_for_model(self.place)
        ReviewFactory.create(
            content_type=self.ct,
            object_id=self.place.id)

    def test_get_all_reviews(self):
        response = self.client.get(reverse('api-place:reviews',
                                   kwargs={'place_pk': self.place.id}))
        reviews = Review.objects.filter(content_type=self.ct,
                                        object_id=self.place.id)
        serializer = ReviewSerializer(reviews, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_empty_reviews_list(self):
        response = self.client.get(reverse('api-place:reviews',
                                   kwargs={'place_pk': self.place2.id}))
        reviews = Review.objects.filter(content_type=self.ct,
                                        object_id=self.place2.id)
        serializer = ReviewSerializer(reviews, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(reviews), 0)


class CreatePlaceReviewTest(APITestCase):
    def setUp(self):
        self.place = PlaceFactory()
        self.url = reverse('api-place:reviews',
                           kwargs={'place_pk': self.place.id})
        self.user = User.objects.create(username="nerd")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.valid_payload = {
            'title': "Great Place!",
            'content': "This was great",
            'rate': 5
        }
        self.invalid_payload = {
            'title': "Great Place!",
            'rate': 5
        }

    def test_create_valid_place_review(self):
        response = self.client.post(self.url,
                                    self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_place_review(self):
        response = self.client.post(self.url,
                                    self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CreateTripReviewTest(APITestCase):
    def setUp(self):
        self.trip = TripFactory()
        self.url = reverse('api-trip:reviews',
                           kwargs={'trip_pk': self.trip.id})
        self.user = User.objects.create(username="nerd")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.valid_payload = {
            'title': "Great Trip!",
            'content': "This was great",
            'rate': 5
        }
        self.invalid_payload = {
            'title': "Great Trip!",
            'rate': 5
        }

    def test_create_valid_trip_review(self):
        response = self.client.post(self.url,
                                    self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_trip_review(self):
        response = self.client.post(self.url,
                                    self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
