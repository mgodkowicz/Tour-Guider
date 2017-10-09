from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from .views import UserCreateAPIView

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^/auth/', obtain_jwt_token),
    url(r'^/token-verify/', verify_jwt_token)
]
