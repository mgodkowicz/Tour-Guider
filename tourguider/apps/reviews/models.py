from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Review(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name='reviews')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __unicode__(self):
        return "{} - {} in {} with id {}".format(
            self.user.username, self.date, self.content_type, self.object_id)

    def __str__(self):
        return "{} - {} in {} with id {}".format(
            self.user.username, self.date, self.content_type, self.object_id)

# print(ContentType.objects.get_for_model(Place))
