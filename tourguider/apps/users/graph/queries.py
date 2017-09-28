import graphene

from .types import UserType, User


class UserQuery(graphene.AbstractType):
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType,
                          id=graphene.Int(),
                          username=graphene.String())

    @graphene.resolve_only_args
    def resolve_all_users(self):
        return User.objects.all()

    @staticmethod
    def resolve_user(self, args, context, info):
        id = args.get('id')
        name = args.get('username')

        if id is not None:
            return User.objects.get(pk=id)

        if name is not None:
            return User.objects.get(username=name)

        return None
