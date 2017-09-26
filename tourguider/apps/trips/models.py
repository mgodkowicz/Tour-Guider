import datetime

from django.db import models
from django.utils import timezone

from apps.places.models import Place
# Create your models here.


class Trip(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    places = models.ManyToManyField(Place)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    rate = models.IntegerField()
    # comments =

    @property
    def duration(self):
        return sum((place.duration for place in self.places.all()), datetime.timedelta())

    @property
    def cost(self):
        return sum((place.cost for place in self.places.all()))

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Trip'
        verbose_name_plural = 'Trips'
