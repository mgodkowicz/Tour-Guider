import graphene
from django.contrib.contenttypes.models import ContentType

from apps.trips.graph.types import TripType
from apps.trips.models import Trip
from apps.places.models import Place
from apps.places.graph.types import PlaceType
from .types import ReviewInputType, ReviewType
from ..models import Review


class CreateTripReview(graphene.Mutation):
    review = graphene.Field(ReviewType)
    trip = graphene.Field(TripType)

    class Input:
        review_data = ReviewInputType()

    @staticmethod
    def mutate(root, input, context, info):
        review_data = input.get('review_data')
        trip = Trip.objects.get(id=review_data.get('object_id'))
        review = Review.objects.create(
            content_type=ContentType.objects.get_for_model(Trip),
            user=context.user,
            **review_data
        )

        return CreateTripReview(review=review, trip=trip)


class CreatePlaceReview(graphene.Mutation):
    review = graphene.Field(ReviewType)
    place = graphene.Field(PlaceType)

    class Input:
        review_data = ReviewInputType()

    @staticmethod
    def mutate(root, input, context, info):
        review_data = input.get('review_data')
        place = Place.objects.get(id=review_data.get('object_id'))
        review = Review.objects.create(
            content_type=ContentType.objects.get_for_model(Place),
            user=context.user,
            **review_data
        )

        return CreatePlaceReview(review=review, place=place)


class ReviewMutation(graphene.AbstractType):
    create_trip_review = CreateTripReview.Field()
    create_place_review = CreatePlaceReview.Field()
