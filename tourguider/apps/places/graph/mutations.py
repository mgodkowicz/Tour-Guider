from datetime import timedelta

import graphene
from graphene_django_extras import DjangoSerializerMutation

from apps.places.models import Place, Guide
from .types import GuideType, GuideInput
from ..serializers import OpeningHourSerializer, PlaceSerializer, GuideSerializer


# class CreatePlace(graphene.Mutation):
#     place = graphene.Field(PlaceType)
#     guide = graphene.Field(GuideType)
#
#     class Arguments:
#         place_data = PlaceInput(required=True)
#         guide_data = GuideInput()
#
#     @staticmethod
#     def mutate(root, info, **kwargs):
#         place_data = kwargs.get('place_data')
#         guide_data = kwargs.get('guide_data')
#
#         duration = timedelta(
#             minutes=place_data.get('duration', 0))
#         place_data['duration'] = duration
#         place = Place(**place_data)
#         place.save()
#         guide = None
#         if guide_data:
#             duration = timedelta(
#                 minutes=guide_data.get('duration', 0))
#             guide = Guide(
#                 name=guide_data.get('name'),
#                 text=guide_data.get('text'),
#                 duration=duration,
#                 audioURL=guide_data.get('audioURL'),
#                 place=place
#             )
#             guide.save()
#
#         return CreatePlace(place=place, guide=guide)
#
#
# class EditPlace(graphene.Mutation):
#     place = graphene.Field(PlaceType)
#
#     class Arguments:
#         place_data = PlaceInput(required=True)
#
#     @staticmethod
#     def mutate(root, info, **kwargs):
#         place_data = kwargs.get('place_data')
#
#         if place_data.get('id'):
#             Place.objects.get(id=place_data.get('id'))
#             place = Place(**place_data)
#             return EditPlace(place=place)
#         return None
#
#
# class DeletePlace(graphene.Mutation):
#     deleted = graphene.Boolean()
#
#     class Arguments:
#         id = graphene.Int()
#
#     @staticmethod
#     def mutate(root, info, **kwargs):
#         # if info.context['user']. isauthenticated
#         place = Place.objects.get(id=kwargs.get('id'))
#         place.delete()
#         return DeletePlace(deleted=True)


class OpeningHoursMutation(DjangoSerializerMutation):
    """
        DjangoSerializerMutation auto implement Create, Delete and Update function
    """

    class Meta:
        description = " Serializer based Mutation for Users "
        serializer_class = OpeningHourSerializer


class PlacesMutation(DjangoSerializerMutation):
    """
        DjangoSerializerMutation auto implement Create, Delete and Update function
    """

    class Meta:
        description = " Serializer based Mutation for Users "
        serializer_class = PlaceSerializer


class PlaceMutation:
    create_place = PlacesMutation.CreateField() #CreatePlace.Field()
    edit_place = PlacesMutation.UpdateField()
    delete_place = PlacesMutation.DeleteField()
    create_hour = OpeningHoursMutation.CreateField(deprecation_reason='Deprecation message')
    edit_hour = OpeningHoursMutation.UpdateField()
    delete_hour = OpeningHoursMutation.DeleteField()
