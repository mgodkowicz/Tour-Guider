from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import graphene
from rest_framework_jwt.settings import api_settings

from .types import UserType


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    @staticmethod
    def mutate(root, info, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        email = kwargs.get('email')

        user = User.objects.create_user(
            username=username, email=email, password=password)

        return CreateUser(user=user)


class LogIn(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()

    class Arguments:
        username = graphene.String()
        password = graphene.String()

    @staticmethod
    def mutate(root, info, **kwargs):

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user = authenticate(
            username=kwargs.get('username'),
            password=kwargs.get('password'),
        )
        if not user:
            raise Exception('Invalid username or password!')

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return LogIn(user=user, token=token)


class UserMutation:
    create_user = CreateUser.Field()
    login = LogIn.Field()
