from rest_framework import serializers
from .models import Booking
from services.models import Service

class BookingSerializer(serializers.ModelSerializer):
    service_ids = serializers.PrimaryKeyRelatedField(many=True, source='services', queryset=Service.objects.all(), write_only=True)

    class Meta:
        model = Booking
        fields = [
            'id', 'user', 'specialist', 'services', 'service_ids',
            'start_datetime', 'end_datetime', 'total_price', 'status',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['services', 'total_price', 'status', 'created_at', 'updated_at']

    def validate(self, attrs):
        start = attrs.get('start_datetime')
        end = attrs.get('end_datetime')
        if start and end:
            # enforce working hours 08:00-18:00
            if start.hour < 8 or end.hour > 18 or end <= start:
                raise serializers.ValidationError('Invalid time window (08:00-18:00).')
        return attrs