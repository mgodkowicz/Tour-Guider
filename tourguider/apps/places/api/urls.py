from django.conf.urls import url

from apps.reviews.api.views import ReviewListAPIView
from .views import PlaceListAPIView, PlaceDetailAPIView, PlaceOpeningHoursAPIView, PlaceGuidesAPIView, \
    PlaceGuideDetailAPIView

urlpatterns = [
    url(r'^$', PlaceListAPIView.as_view(), name='list'),
    url(r'^(?P<place_pk>[0-9]+)/$', PlaceDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<place_pk>[0-9]+)/hours/$', PlaceOpeningHoursAPIView.as_view(), name='hours'),
    url(r'^(?P<place_pk>[0-9]+)/guides/$', PlaceGuidesAPIView.as_view(), name='guides'),
    url(r'^(?P<place_pk>[0-9]+)/guides/(?P<guide_pk>[0-9]+)/$', PlaceGuideDetailAPIView.as_view(), name='guide-detail'),
    url(r'^(?P<place_pk>[0-9]+)/reviews/$', ReviewListAPIView.as_view(),  {'type': 'place'}, name='reviews')
]
