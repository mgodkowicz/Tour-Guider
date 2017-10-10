from django.contrib.contenttypes.models import ContentType
from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.places.models import Place
from apps.reviews.api.serializers import ReviewSerializer
from apps.reviews.models import Review
from apps.trips.models import Trip


class ReviewListAPIView(ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        pk, obj = self.object_type()
        instance = get_object_or_404(obj, id=pk)
        ct = ContentType.objects.get_for_model(obj)
        return Review.objects.filter(object_id=instance.id, content_type=ct)

    def object_type(self):
        arg = self.kwargs.get('trip_pk', False)
        if arg:
            return arg, Trip
        return self.kwargs.get('pk'), Place
