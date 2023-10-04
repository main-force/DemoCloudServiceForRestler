from rest_framework import serializers
from .models import Subscription
from user_profile.models import UserProfile


class SubscriptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'name']  # user_profile은 제외


class SubscriptionListRetrieveSerializer(serializers.ModelSerializer):
    user_profile = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())

    class Meta:
        model = Subscription
        fields = ['id', 'name', 'user_profile']
