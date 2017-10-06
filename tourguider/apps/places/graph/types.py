import graphene
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
#from graphene_django import DjangoObjectType
from graphene_django_extras import DjangoObjectType, DjangoListObjectType

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

    def resolve_reviews(self):
        return Review.objects.filter(
            content_type=ContentType.objects.get_for_model(Place), object_id=self.id)


class GuideType(DjangoObjectType):
    duration = graphene.String(source="duration")

    class Meta:
        model = Guide


# class PlaceInput(graphene.InputObjectType):
#     id = graphene.Int(required=False)
#     name = graphene.String()
#     description = graphene.String()
#     duration = graphene.Int()
#     city = graphene.String()
#     address = graphene.String()
#     latitude = graphene.String()
#     longitude = graphene.String()
#     cost = graphene.Int()
#
#
# class PlaceEditInput(graphene.InputObjectType):
#     id = graphene.Int()
#     name = graphene.String(required=False)
#     description = graphene.String(required=False)
#     duration = graphene.Int(required=False)
#     city = graphene.String(required=False)
#     address = graphene.String(required=False)
#     latitude = graphene.String(required=False)
#     longitude = graphene.String(required=False)
#     cost = graphene.Int(required=False)

from graphene_django_extras import DjangoInputObjectType


# class PlaceInput(DjangoInputObjectType):
#     class Meta:
#         description = " Place Input Type for used as input on Arguments classes on traditional Mutations "
#         model = Place
#
# class GuideInput(DjangoInputObjectType):
#     class Meta:
#         description = " Place Input Type for used as input on Arguments classes on traditional Mutations "
#         model = Guide


class GuideInput(graphene.InputObjectType):
    name = graphene.String()
    duration = graphene.Int()
    audioURL = graphene.String()
    place = graphene.Int()
    text = graphene.String()
