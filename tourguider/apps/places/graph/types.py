import graphene
from graphene_django import DjangoObjectType

from apps.places.models import Place, Guide


class PlaceType(DjangoObjectType):
    duration = graphene.String(source="duration")

    class Meta:
        model = Place


class GuideType(DjangoObjectType):
    duration = graphene.String(source="duration")

    class Meta:
        model = Guide


class PlaceInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    #   guide = graphene.String()
    duration = graphene.Int()
    city = graphene.String()
    address = graphene.String()
    latitude = graphene.String()
    longitude = graphene.String()
    cost = graphene.Int()


class GuideInput(graphene.InputObjectType):
    name = graphene.String()
    duration = graphene.Int()
    audioURL = graphene.String()
    place = graphene.Int()
