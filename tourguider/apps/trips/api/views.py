from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..models import Trip
from .serializers import TripSerializer


class IsAuthenticatedNotPost(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return super(IsAuthenticatedNotPost, self).has_permission(request, view)


class TripListAPIView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = (IsAuthenticatedNotPost,)


class TripDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    lookup_url_kwarg = 'trip_pk'
    permission_classes = (IsAuthenticatedNotPost,)
