from rest_framework import serializers
from .models import ServiceCategory, Service

class ServiceCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = ServiceCategory
    fields = ["id", "name"]

class ServiceSerializer(serializers.ModelSerializer):
  category = ServiceCategorySerializer(read_only=True)
  category_id = serializers.PrimaryKeyRelatedField(source="category", queryset=ServiceCategory.objects.all(), write_only=True)

  class Meta:
    model = Service
    fields = ["id", "category", "category_id", "name", "description", "duration_min", "default_price"]