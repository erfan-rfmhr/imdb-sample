from .models import Rate
from rest_framework import serializers

class RateSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(min_value=1, max_value=10)
    class Meta:
        model = Rate
        fields = ['id', 'score', 'movie', 'user', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
