from django.conf.urls import url

from apps.places.api.views import TripPlacesAPIView
from apps.reviews.api.views import ReviewListAPIView
from .views import TripListAPIView, TripDetailAPIView

urlpatterns = [
    url(r'^$', TripListAPIView.as_view(), name='list'),
    url(r'^(?P<trip_pk>[0-9]+)/$', TripDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<trip_pk>[0-9]+)/places/$', TripPlacesAPIView.as_view(), name='places-list'),
    url(r'^(?P<trip_pk>[0-9]+)/reviews/$', ReviewListAPIView.as_view(), name='reviews'),

]
