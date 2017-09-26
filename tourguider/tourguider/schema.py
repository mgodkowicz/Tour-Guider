import graphene
from graphene_django.views import GraphQLView
import rest_framework
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.trips.schema import TripQuery, TripMutation
from apps.places.schema import PlaceQuery, PlaceMutation


class PublicQuery(TripQuery, PlaceQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class PrivateQuery(PlaceQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(PlaceMutation, TripMutation, graphene.ObjectType):
    pass

public_schema = graphene.Schema(query=PublicQuery, mutation=Mutation)

private_schema = graphene.Schema(query=PrivateQuery, mutation=Mutation)


class DRFAuthenticatedGraphQLView(GraphQLView):
    # custom view for using DRF TokenAuthentication with graphene GraphQL.as_view()
    # all requests to Graphql endpoint will require token for auth, obtained from DRF endpoint
    # https://github.com/graphql-python/graphene/issues/249

    def parse_body(self, request):
        if isinstance(request, rest_framework.request.Request):
            return request.data
        return super(GraphQLView, self).parse_body(request)

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(GraphQLView, cls).as_view(*args, **kwargs)
        view = permission_classes((IsAuthenticated,))(view)
        view = authentication_classes((JSONWebTokenAuthentication, ))(view)
        view = api_view(['GET', 'POST'])(view)
        return view
