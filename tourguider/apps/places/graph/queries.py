import graphene

from apps.places.models import Place, OpeningHour
from .types import PlaceType


class PlaceQuery:
    all_places = graphene.List(PlaceType)
    place = graphene.Field(PlaceType,
                           id=graphene.Int(),
                           name=graphene.String())

    @staticmethod
    def resolve_all_places(self, info, **kwargs):
        return Place.objects.all()

    @staticmethod
    def resolve_place(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Place.objects.get(pk=id)

        if name is not None:
            return Place.objects.get(name=name)

        return None
