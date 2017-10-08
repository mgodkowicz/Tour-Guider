from django.conf.urls import url

from .views import PlaceListAPIView, PlaceDetailAPIView, PlaceOpeningHoursAPIView, PlaceGuidesAPIView

urlpatterns = [
    url(r'^$', PlaceListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', PlaceDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/hours/$', PlaceOpeningHoursAPIView.as_view(), name='hours'),
    url(r'^(?P<pk>[0-9]+)/guides/$', PlaceGuidesAPIView.as_view(), name='guides'),

]
