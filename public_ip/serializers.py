from rest_framework import serializers
from .models import PublicIP


class PublicIPRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicIP
        fields = ['id', 'name', 'subscription']


class PublicIPCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicIP
        fields = ['id', 'name']

