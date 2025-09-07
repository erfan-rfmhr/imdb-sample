from rest_framework import serializers

from .models import Rate


class RateCreateSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(min_value=1, max_value=10)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rate
        fields = ['id', 'score', 'movie', 'user', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        rate = super().create(validated_data)

        movie_owner = rate.movie.user
        movie_owner.notify_new_rate(rate)
        return rate

class RateSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Rate
        fields = ['id', 'score', 'movie', 'user', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
