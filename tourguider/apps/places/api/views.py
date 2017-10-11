from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.places.api.serializers import PlaceSerializer, OpeningHourSerializer, GuideSerializer, PlaceDetailSerializer
from apps.places.models import Place, OpeningHour, Guide
from apps.trips.api.permissions import IsAdminOrReadOnly
from apps.trips.models import Trip


class PlaceListAPIView(generics.ListCreateAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = (IsAdminOrReadOnly,)


class PlaceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlaceDetailSerializer
    queryset = Place.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    lookup_url_kwarg = 'place_pk'


class PlaceOpeningHoursAPIView(generics.ListCreateAPIView):
    """
    post:
        if place doesn't have specific weekday opening hour
        create new instance otherwise update old one
    """
    serializer_class = OpeningHourSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        place = get_object_or_404(Place, id=self.kwargs['place_pk'])
        return place.hours

    def perform_create(self, serializer):
        serializer.save(
            place=self.kwargs['place_pk']
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
        place = get_object_or_404(Place, id=self.kwargs['place_pk'])
        guides = Guide.objects.filter(place=place)
        return guides

    def perform_create(self, serializer):
        place = get_object_or_404(Place, id=self.kwargs['place_pk'])
        serializer.save(
            place=place
        )


class PlaceGuideDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GuideSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_url_kwarg = 'place_pk'

    def get_object(self):
        guide = get_object_or_404(
            Guide, id=self.kwargs['guide_pk'], place=self.kwargs['place_pk'])
        return guide
