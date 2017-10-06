from rest_framework import serializers

from ..models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'name', 'description',
                  'cost', 'duration', 'rate')


class TripDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'name', 'description',
                  'cost', 'duration', 'rate', 'places')
