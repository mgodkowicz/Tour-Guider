from django.conf.urls import url

from apps.places.api.views import TripPlacesAPIView
from .views import TripListAPIView, TripDetailAPIView

urlpatterns = [
    url(r'^$', TripListAPIView.as_view(), name='list'),
    url(r'^(?P<trip_pk>[0-9]+)/$', TripDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<trip_pk>[0-9]+)/places/$', TripPlacesAPIView.as_view(), name='places-list')

]
