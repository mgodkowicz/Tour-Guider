"""tourguider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from graphene_django.views import GraphQLView
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from .schema import public_schema


urlpatterns = [
    url(r'^api/token-auth/', obtain_jwt_token),
    url(r'^api/token-verify/', verify_jwt_token),
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^graphql/', GraphQLView.as_view(graphiql=True, schema=public_schema)),

    url(r'^api/trips/', include('apps.trips.api.urls', namespace='api-trip')),
    url(r'^api/places/', include('apps.places.api.urls', namespace='api-place')),

    url(r'^api/docs/', include('rest_framework_docs.urls')),
    url(r'^api/docs2/', include_docs_urls(title='My API title'))

]
