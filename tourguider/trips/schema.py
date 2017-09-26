import graphene

from graphene_django import DjangoObjectType

from .models import Trip
from places.models import Place


class PlaceType(DjangoObjectType):
    class Meta:
        model = Place


class TripType(DjangoObjectType):
    places = graphene.List(PlaceType)

    class Meta:
        model = Trip

    @graphene.resolve_only_args
    def resolve_places(self):
        return self.places.all()


class Query(graphene.AbstractType):
    trip = graphene.Field(TripType,
                          id=graphene.Int(),
                          name=graphene.String())
    all_trips = graphene.List(TripType)

    all_places = graphene.List(PlaceType)
    place = graphene.Field(PlaceType,
                           id=graphene.Int(),
                           name=graphene.String())

    def resolve_all_trips(self, args, context, info):
        return Trip.objects.all()

    # def resolve_places(self, info, *args, **kwargs):
    #     return Place.objects.all()

    def resolve_trip(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Trip.objects.get(pk=id)

        if name is not None:
            return Trip.objects.get(name=name)

        return None

    def resolve_place(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Place.objects.get(pk=id)

        if name is not None:
            return Place.objects.get(name=name)

        return None
