import graphene

from apps.places.models import Place
from apps.trips.graph.types import TripType
from apps.trips.models import Trip


class CreateTrip(graphene.Mutation):
    trip = graphene.Field(TripType)

    class Arguments:
        name = graphene.String()
        description = graphene.String()
        places = graphene.List(graphene.Int)

    @staticmethod
    def mutate(root, info, **kwargs):
        places = Place.objects.filter(id__in=kwargs.get('places', []))
        trip = Trip(
            name=kwargs.get('name'),
            description=kwargs.get('description')
        )
        trip.save()
        trip.places.add(*list(places))

        return CreateTrip(trip=trip)


class TripMutation:
    create_trip = CreateTrip.Field()
