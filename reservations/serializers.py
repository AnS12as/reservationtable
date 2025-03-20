from rest_framework import serializers
from .models import Table, Booking


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ["id", "user", "name", "phone", "table", "date", "time", "guests", "status"]
