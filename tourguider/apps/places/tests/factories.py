from django.utils.timezone import timedelta
from factory import Sequence
from factory.django import DjangoModelFactory, ImageField

from apps.places.models import Place, Guide, OpeningHour


class PlaceFactory(DjangoModelFactory):
    class Meta:
        model = Place

    name = Sequence(lambda n: "Place %03d" % n)
    description = "description"
    duration = timedelta(minutes=30)
    latitude = 51.10922092338914
    longitude = 17.031168937683105
    cost = 15.5


class GuideFactory(DjangoModelFactory):
    class Meta:
        model = Guide

    name = Sequence(lambda n: "Guide %03d" % n)
    text = "text"
    audioURL = "www.example.com"
    duration = timedelta(minutes=11)
    place = PlaceFactory()
