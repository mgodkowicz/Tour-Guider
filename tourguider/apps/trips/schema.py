import graphene
from graphene_django import DjangoObjectType

from apps.places.models import Place
from apps.places.graph.types import PlaceType
from .models import Trip


class TripType(DjangoObjectType):
    places = graphene.List(PlaceType)
    cost = graphene.Int(source="cost")
    duration = graphene.String(source="duration")

    class Meta:
        model = Trip

    @graphene.resolve_only_args
    def resolve_places(self):
        return self.places.all()


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
        return Trip.objects.all()

    @staticmethod
    def resolve_trip(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Trip.objects.get(pk=id)

        if name is not None:
            return Trip.objects.get(name=name)

        return None


class CreateTrip(graphene.Mutation):
    trip = graphene.Field(TripType)

    class Input:
        name = graphene.String()
        description = graphene.String()
        places = graphene.List(graphene.Int)

    @staticmethod
    def mutate(root, input, context, info):
        places = Place.objects.filter(id__in=input.get('places', []))
        trip = Trip(
            name=input.get('name'),
            description=input.get('description')
        )
        trip.save()
        trip.places.add(*list(places))

        return CreateTrip(trip=trip)


class TripMutation(graphene.AbstractType):
    create_trip = CreateTrip.Field()
