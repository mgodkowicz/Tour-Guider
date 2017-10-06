import datetime

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

from apps.places.models import Place
from apps.reviews.models import Review


class Trip(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    places = models.ManyToManyField(Place, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    @property
    def duration(self):
        return sum((place.duration for place in self.places.all()), datetime.timedelta())

    @property
    def cost(self):
        return sum((place.cost for place in self.places.all()))

    @property
    def rate(self):
        reviews = Review.objects.filter(
            content_type=ContentType.objects.get_for_model(Trip), object_id=self.id)
        if len(reviews):
            return sum(review.rate for review in reviews) / len(reviews)
        return 0

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Trip'
        verbose_name_plural = 'Trips'
