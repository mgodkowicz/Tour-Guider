import graphene

from apps.places.graph.types import PlaceType
from apps.trips.graph.types import TripType
from apps.trips.models import Trip


class TripQuery(graphene.AbstractType):
    trip = graphene.Field(TripType,
                          id=graphene.Int(),
                          name=graphene.String())
    all_trips = graphene.List(TripType)

    all_places = graphene.List(PlaceType)
    place = graphene.Field(PlaceType,
                           id=graphene.Int(),
                           name=graphene.String())

    @staticmethod
    def resolve_all_trips(self, args, context, info):
        return Trip.objects.all() # select_related('reviews').all()

    @staticmethod
    def resolve_trip(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Trip.objects.get(pk=id)

        if name is not None:
            return Trip.objects.get(name=name)

        return None
