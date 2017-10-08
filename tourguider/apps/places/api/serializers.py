from rest_framework import serializers

from apps.places.models import OpeningHour, Place, Guide


class OpeningHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = '__all__'

    def create(self, validated_data):
        place_id = validated_data['place']
        hour = OpeningHour.objects.create(
            **validated_data
        )
        place = Place.objects.get(id=place_id)
        place.hours.add(hour)
        return hour


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'
        read_only_fields = ('place',)


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
        read_only_fields = ('created',)


class PlaceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = '__all__'
        read_only_fields = ('created',)
