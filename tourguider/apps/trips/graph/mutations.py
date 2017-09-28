import graphene

from apps.places.models import Place
from apps.trips.graph.types import TripType
from apps.trips.models import Trip


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
