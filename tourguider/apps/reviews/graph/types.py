import graphene
from graphene_django import DjangoObjectType

from ..models import Review


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review


class ReviewInputType(graphene.InputObjectType):
    title = graphene.String()
    content = graphene.String()
    rate = graphene.Int()
    object_id = graphene.Int()
