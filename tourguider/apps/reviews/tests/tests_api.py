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
                                   kwargs={'pk': self.place.id}))
        reviews = Review.objects.filter(content_type=self.ct,
                                        object_id=self.place.id)
        serializer = ReviewSerializer(reviews, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_empty_reviews_list(self):
        response = self.client.get(reverse('api-place:reviews',
                                   kwargs={'pk': self.place2.id}))
        reviews = Review.objects.filter(content_type=self.ct,
                                        object_id=self.place2.id)
        serializer = ReviewSerializer(reviews, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(reviews), 0)
