from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Advertisement
from .models import AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""
    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        user = self.context['request'].user
        open_ads_count = Advertisement.objects.filter(creator=user, status=AdvertisementStatusChoices.OPEN).count()
        if open_ads_count >= 10:
            raise serializers.ValidationError('У вас не может быть больше 10 открытых объявлений')
        validated_data['creator'] = user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        if self.instance and self.instance.creator != self.context['request'].user:
            raise serializers.ValidationError("Вы можете редактировать только свои объявления.")
        return data
