from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.places.api.serializers import PlaceSerializer, OpeningHourSerializer, GuideSerializer
from apps.places.models import Place, OpeningHour, Guide
from apps.trips.api.permissions import IsAdminOrReadOnly
from apps.trips.models import Trip


class PlaceListAPIView(generics.ListCreateAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = (IsAdminOrReadOnly,)


class PlaceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = (IsAdminOrReadOnly,)


class PlaceOpeningHoursAPIView(generics.ListCreateAPIView):
    serializer_class = OpeningHourSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        place = Place.objects.get(id=self.kwargs['pk'])
        return place.hours

    def perform_create(self, serializer):
        serializer.save(
            place=self.kwargs['pk']
        )


class TripPlacesAPIView(generics.ListAPIView):
    serializer_class = PlaceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        trip = Trip.objects.get(id=self.kwargs['trip_pk'])
        return trip.places


class PlaceGuidesAPIView(generics.ListCreateAPIView):
    serializer_class = GuideSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        try:
            place = Place.objects.get(id=self.kwargs['pk'])
            guides = Guide.objects.filter(place=place)
        except:
            raise Http404
        return guides

    def perform_create(self, serializer):
        try:
            place = Place.objects.get(id=self.kwargs['pk'])
        except:
            raise Http404
        serializer.save(
            place=place
        )
