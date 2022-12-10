from rest_framework import serializers

from carshare_v2.transports.models import Transport


class TransportSerializer(serializers.ModelSerializer):
    from_city_name = serializers.CharField(source='from_city', read_only=True)
    to_city_name = serializers.CharField(source='to_city', read_only=True)
    driver_first_name = serializers.CharField(source='driver.profile.first_name', read_only=True)
    driver_last_name = serializers.CharField(source='driver.profile.last_name', read_only=True)
    passengers_count = serializers.CharField(source='passengers.count', read_only=True)

    class Meta:
        model = Transport
        fields = ['id', 'from_city_name', 'to_city_name', 'driver_id', 'driver_first_name', 'driver_last_name', 'description', 'date', 'time', 'total_seats',
                  'passengers_count', 'status']
