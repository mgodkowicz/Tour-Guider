import graphene

from apps.places.models import Place
from .types import PlaceType


class PlaceQuery(graphene.AbstractType):
    all_places = graphene.List(PlaceType)
    place = graphene.Field(PlaceType,
                           id=graphene.Int(),
                           name=graphene.String())

    @staticmethod
    def resolve_all_places(self, args, context, info):
        return Place.objects.all()

    @staticmethod
    def resolve_place(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Place.objects.get(pk=id)

        if name is not None:
            return Place.objects.get(name=name)

        return None
