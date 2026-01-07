from rest_framework import serializers
from .models import Province, City, Village


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ["id", "name", "created_at", "updated_at"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "name", "province", "created_at", "updated_at"]


class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = ["id", "name", "city", "created_at", "updated_at"]
