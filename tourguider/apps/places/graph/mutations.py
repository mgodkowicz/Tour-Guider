from datetime import timedelta

import graphene

from apps.places.models import Place, Guide
from .types import PlaceType, GuideType, PlaceInput, GuideInput


class CreatePlace(graphene.Mutation):
    place = graphene.Field(PlaceType)
    guide = graphene.Field(GuideType)

    class Input:
        place_data = PlaceInput(required=True)
        guide_data = GuideInput()

    @staticmethod
    def mutate(root, input, context, info):
        place_data = input.get('place_data')
        guide_data = input.get('guide_data')

        duration = timedelta(
            minutes=place_data.get('duration', 0))
        place_data['duration'] = duration
        place = Place(**place_data)
        place.save()
        guide = None
        if guide_data:
            duration = timedelta(
                minutes=guide_data.get('duration', 0))
            guide = Guide(
                name=guide_data.get('name'),
                text=guide_data.get('text'),
                duration=duration,
                audioURL=guide_data.get('audioURL'),
                place=place
            )
            guide.save()

        return CreatePlace(place=place, guide=guide)


class PlaceMutation(graphene.AbstractType):
    create_place = CreatePlace.Field()


    # name=place_data.name,
    # description=place_data.description,
    # duration=duration,
    # #guide=input.get('guide'),
    # city=place_data.city,
    # address=place_data.address,
    # # latitude=input.get('latitude', 0),
    # # longitude=input.get('longitude', 0),
    # # cost=input.get('cost', 0)
    # name=place_data.get('name'),
    # description=place_data.get('description'),
    # duration=duration,
    # city=place_data.get('city', 'Wrocław'),
    # address=place_data.get('address'),
    # latitude=place_data.get('latitude', 0),
    # longitude=place_data.get('longitude', 0),
    # cost=place_data.get('cost', 0)
