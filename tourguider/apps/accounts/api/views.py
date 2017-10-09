from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """
    Creates the user.
    """
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
