import graphene

from apps.trips.schema import TripQuery
from apps.places.schema import PlaceQuery


class Query(TripQuery, PlaceQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
