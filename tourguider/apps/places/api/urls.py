from django.conf.urls import url

from .views import PlaceListAPIView, PlaceDetailAPIView, PlaceOpeningHoursAPIView, PlaceGuidesAPIView, \
    PlaceGuideDetailAPIView

urlpatterns = [
    url(r'^$', PlaceListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', PlaceDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/hours/$', PlaceOpeningHoursAPIView.as_view(), name='hours'),
    url(r'^(?P<pk>[0-9]+)/guides/$', PlaceGuidesAPIView.as_view(), name='guides'),
    url(r'^(?P<pk>[0-9]+)/guides/(?P<guide_pk>[0-9]+)/$', PlaceGuideDetailAPIView.as_view(), name='guide-detail'),

]