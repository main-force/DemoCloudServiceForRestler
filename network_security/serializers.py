from rest_framework import serializers
from .models import NetworkSecurityGroup, NetworkSecurityPolicy
from subscription.serializers import \
    SubscriptionListRetrieveSerializer  # SubscriptionListRetrieveSerializer가 정의된 곳에서 가져와야 합니다.


# NetworkSecurityGroup Serializer
class NetworkSecurityGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkSecurityGroup
        fields = ['id', 'name']  # subscription을 포함하여야 ForeignKey로 설정되어있기 때문입니다.


class NetworkSecurityGroupListRetrieveSerializer(serializers.ModelSerializer):
    subscription = SubscriptionListRetrieveSerializer(read_only=True)  # Nested Serializer로 Subscription의 detail을 포함합니다.

    class Meta:
        model = NetworkSecurityGroup
        fields = ['id', 'name', 'subscription']


# NetworkSecurityPolicy Serializer
class NetworkSecurityPolicyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkSecurityPolicy
        fields = ['id', 'name']  # network_security_group를 포함하여야 ForeignKey로 설정되어있기 때문입니다.


class NetworkSecurityPolicyListRetrieveSerializer(serializers.ModelSerializer):
    network_security_group = NetworkSecurityGroupListRetrieveSerializer(
        read_only=True)  # Nested Serializer로 NetworkSecurityGroup의 detail을 포함합니다.

    class Meta:
        model = NetworkSecurityPolicy
        fields = ['id', 'name', 'network_security_group']
