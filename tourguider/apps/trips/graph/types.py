import graphene
from django.contrib.contenttypes.models import ContentType
from graphene_django import DjangoObjectType

from apps.places.graph.types import PlaceType
from apps.reviews.graph.types import ReviewType
from apps.reviews.models import Review
from apps.trips.models import Trip


class TripType(DjangoObjectType):
    places = graphene.List(PlaceType)
    cost = graphene.Float(source="cost")
    rate = graphene.Float(source="rate")
    duration = graphene.String(source="duration")
    reviews = graphene.List(ReviewType)

    class Meta:
        model = Trip

    @graphene.resolve_only_args
    def resolve_places(self):
        return self.places.all()

    @graphene.resolve_only_args
    def resolve_reviews(self):
        return Review.objects.filter(content_type=ContentType.objects.get_for_model(Trip), object_id=self.id)
