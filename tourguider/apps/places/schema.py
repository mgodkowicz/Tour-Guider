from datetime import timedelta
import graphene
from graphene_django import DjangoObjectType

from .models import Place


class PlaceType(DjangoObjectType):
    duration = graphene.String(source="duration")

    class Meta:
        model = Place


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


class CreatePlace(graphene.Mutation):
    place = graphene.Field(PlaceType)

    class Input:
        name = graphene.String()
        description = graphene.String()
        guide = graphene.String()
        duration = graphene.Int()
        city = graphene.String()
        address = graphene.String()
        latitude = graphene.String()
        longitude = graphene.String()
        cost = graphene.Int()

    @staticmethod
    def mutate(root, input, context, info):
        duration = timedelta(
            minutes=input.get('duration'))

        place = Place(
            name=input.get('name'),
            description=input.get('description'),
            duration=duration,
            guide=input.get('guide'),
            city=input.get('city', 'Wrocław'),
            address=input.get('address'),
            latitude=input.get('latitude', 0),
            longitude=input.get('longitude', 0),
            cost=input.get('cost', 0)
        )
        place.save()

        return CreatePlace(place=place)


class PlaceMutation(graphene.AbstractType):
    create_place = CreatePlace.Field()
