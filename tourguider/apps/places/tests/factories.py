from django.utils.timezone import timedelta
from factory import Sequence
from factory.django import DjangoModelFactory, ImageField

from apps.places.models import Place


class PlaceFactory(DjangoModelFactory):
    class Meta:
        model = Place

    name = Sequence(lambda n: "Place %03d" % n)
    description = "description"
    duration = timedelta(minutes=30)
    latitude = 51.10922092338914
    longitude = 17.031168937683105
    cost = 15.5
