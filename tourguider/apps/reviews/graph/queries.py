# print(ContentType.objects.get_for_model(Place))
import graphene

from .types import ReviewType
from ..models import Review


class ReviewQuery(graphene.AbstractType):
    all_reviews = graphene.List(ReviewType)
    review = graphene.Field(ReviewType,
                            id=graphene.Int(),
                            title=graphene.String())

    @staticmethod
    def resolve_all_reviews(self, args, context, info):
        return Review.objects.all()

    @staticmethod
    def resolve_review(self, args, context, info):
        id = args.get('id')
        title = args.get('title')

        if id is not None:
            return Review.objects.get(pk=id)

        if title is not None:
            return Review.objects.get(title=title)

        return None
