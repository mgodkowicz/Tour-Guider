from django.db import models
from django.utils import timezone


class OpeningHour(models.Model):
    WEEKDAYS = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]

    weekday = models.IntegerField(choices=WEEKDAYS)
    opening_hour = models.TimeField(blank=True, null=True)
    closing_hour = models.TimeField(blank=True, null=True)
   # open_all_day = models.BooleanField(blank=True)

    class Meta:
        ordering = ('weekday', 'opening_hour')
        unique_together = ('weekday', 'opening_hour', 'closing_hour')

    def __unicode__(self):
        return "{}: {} - {}".format(self.get_weekday_display(), self.opening_hour, self.closing_hour)

    def __str__(self):
        return "{}: {} - {}".format(self.get_weekday_display(), self.opening_hour, self.closing_hour)


class Place(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    duration = models.DurationField()
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=150, blank=True)
    rate = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to='media')
    latitude = models.CharField(max_length=20, blank=True)
    longitude = models.CharField(max_length=20, blank=True)
    cost = models.FloatField(default=0)
    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    hours = models.ManyToManyField(OpeningHour, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'


class Guide(models.Model):
    name = models.CharField(max_length=200)
    audioURL = models.URLField()
    duration = models.DurationField()
    place = models.ForeignKey(Place, related_name='guides')


