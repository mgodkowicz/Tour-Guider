from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from apps.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ('id', 'title', 'content',
                  'rate', 'user', 'date')
        read_only = ('date',)

