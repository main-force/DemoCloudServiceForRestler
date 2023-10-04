from rest_framework import serializers
from .models import StorageAccount


class StorageAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = StorageAccount
        fields = ['id', 'name', 'subscription']


class StorageAccountCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = StorageAccount
        fields = ['id', 'name']
