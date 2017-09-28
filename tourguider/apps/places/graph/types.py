import graphene
from django.contrib.contenttypes.models import ContentType
from graphene_django import DjangoObjectType

from apps.places.models import Place, Guide
from apps.reviews.graph.types import ReviewType
from apps.reviews.models import Review
from apps.trips.models import Trip


class PlaceType(DjangoObjectType):
    duration = graphene.String(source="duration")
    rate = graphene.Float(source="rate")
    reviews = graphene.List(ReviewType)

    class Meta:
        model = Place

    @graphene.resolve_only_args
    def resolve_reviews(self):
        return Review.objects.filter(
            content_type=ContentType.objects.get_for_model(Place), object_id=self.id)


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
