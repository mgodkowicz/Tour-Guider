from django.db import models
from django.utils import timezone


class Place(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    guide = models.TextField()
    duration = models.DurationField()
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=150, blank=True)
    # audio = models
    rate = models.IntegerField(blank=True, null=True)
    # comments =
    photo = models.ImageField(blank=True, upload_to='media')
    latitude = models.CharField(max_length=20, blank=True)
    longitude = models.CharField(max_length=20, blank=True)
    cost = models.FloatField(default=0)
    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
