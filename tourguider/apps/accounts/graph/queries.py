import graphene

from .types import UserType, User


def get_user(context):
    try:
        if context.user.is_authenticated():
            return User.objects.get(pk=context.user.pk)
        raise Exception('Not authenticated')
    except:
        raise Exception('User not found!')


class UserQuery:
    all_users = graphene.List(UserType)
    me = graphene.Field(UserType)
    user = graphene.Field(UserType,
                          id=graphene.Int(),
                          username=graphene.String())

    def resolve_all_users(self, *args):
        return User.objects.all()

    @staticmethod
    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('username')

        if id is not None:
            return User.objects.get(pk=id)

        if name is not None:
            return User.objects.get(username=name)

        return None

    @staticmethod
    def resolve_me(self, info, **kwargs):
        user = get_user(info.context)
        if not user:
            raise Exception('Not logged!')

        return user
