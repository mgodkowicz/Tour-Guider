from factory import Sequence, SubFactory, post_generation
from factory.django import DjangoModelFactory

from apps.places.tests.factories import PlaceFactory
from apps.trips.models import Trip


class TripFactory(DjangoModelFactory):
    class Meta:
        model = Trip

    name = Sequence(lambda n: "Trip %03d" % n)
    description = "description"
    places = SubFactory(PlaceFactory)

    @post_generation
    def places(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for place in extracted:
                self.places.add(place)
