from rest_framework import serializers

from apps.places.models import OpeningHour, Place, Guide


class OpeningHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = '__all__'

    def create(self, validated_data):
        place_id = validated_data['place']
        place = Place.objects.get(id=place_id)
        validated_data.pop('place', None)
        old_hour = self.is_weekday_in_place_hours_set(place, validated_data)
        if old_hour:
            place.hours.remove(old_hour)

        hour, created = OpeningHour.objects.get_or_create(
            **validated_data
        )
        hour.save()
        place.hours.add(hour)
        return hour

    @staticmethod
    def is_weekday_in_place_hours_set(place, validated_data):
        for hour in place.hours.all():
            if hour.weekday == validated_data['weekday']:
                return hour
        return False


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'
        read_only_fields = ('place',)


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'duration', 'city',
                  'address', 'photo', 'latitude', 'longitude',
                  'cost', 'hours', 'is_open')


class PlaceDetailSerializer(serializers.ModelSerializer):
    hours = OpeningHourSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'duration', 'city',
                  'address', 'photo', 'latitude', 'longitude',
                  'cost', 'is_open', 'hours')
