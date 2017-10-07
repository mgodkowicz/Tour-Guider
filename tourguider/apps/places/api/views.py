from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.places.api.serializers import PlaceSerializer, OpeningHourSerializer
from apps.places.models import Place, OpeningHour
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
        places = Place.objects.get(id=self.kwargs['pk'])
        return places.hours


class TripPlacesAPIView(generics.ListAPIView):
    serializer_class = PlaceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        trip = Trip.objects.get(id=self.kwargs['trip_pk'])
        return trip.places
