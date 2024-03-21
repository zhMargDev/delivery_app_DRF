from rest_framework import serializers

from .models import *

# Сериализатор для моделт "Груз"
class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ('id', 'loc_pick_up', 'loc_delivery', 'weight', 'description')

# Сериализатор для модели "Машина"
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'current_location', 'carrying_capacity', 'serial_number')

# Сериализатор для модели "Локация"
class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = ('id', 'city', 'state', 'zip_code', 'latitude', 'longitude')