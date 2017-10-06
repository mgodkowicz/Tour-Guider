from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.trips.api.permissions import IsAuthenticatedNotPost
from .serializers import TripSerializer, TripDetailSerializer
from ..models import Trip


class TripListAPIView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        private = serializer.validated_data.get('private', True)
        if not self.request.user.is_superuser:
            private = True

        serializer.save(author=self.request.user, private=private)


class TripDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripDetailSerializer
    lookup_url_kwarg = 'trip_pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)
