from django.contrib.auth.models import User
from factory import Sequence
from factory.django import DjangoModelFactory

from ..models import Review


class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = Review

    title = Sequence(lambda n: "Trip %03d" % n)
    content = "Great Trip!"
    rate = 5
    user = User.objects.get(id=1)
