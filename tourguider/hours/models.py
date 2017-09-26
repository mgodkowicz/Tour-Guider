from django.db import models

# Create your models here.


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
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()

    class Meta:
        ordering = ('weekday', 'opening_hour')
        unique_together = ('weekday', 'opening_hour', 'closing_hour')

    def __unicode__(self):
        return "{}: {} - {}".format(self.get_weekday_display(), self.opening_hour, self.closing_hour)

    def __str__(self):
        return "{}: {} - {}".format(self.get_weekday_display(), self.opening_hour, self.closing_hour)

