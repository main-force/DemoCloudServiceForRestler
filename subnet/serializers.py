from rest_framework import serializers
from .models import Subnet


class SubnetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subnet
        fields = ['id', 'name', 'subscription', 'public_ip']


class SubnetCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subnet
        fields = ['id', 'name']
