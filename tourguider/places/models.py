from django.db import models
from django.utils import timezone
# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    guide = models.TextField()
    duration = models.DurationField()
    # audio = models
    rate = models.IntegerField()
    # comments =
    photo = models.ImageField()
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    cost = models.FloatField()
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
