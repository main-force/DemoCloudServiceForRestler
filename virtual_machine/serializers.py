from rest_framework import serializers

from network_security.models import NetworkSecurityGroup
from public_ip.models import PublicIP
from storage.models import Storage
from subnet.models import Subnet
from subscription.models import Subscription
from .models import VirtualMachine


class VirtualMachineCreateSerializer(serializers.ModelSerializer):
    public_ip = serializers.PrimaryKeyRelatedField(queryset=PublicIP.objects.all())
    subnet = serializers.PrimaryKeyRelatedField(queryset=Subnet.objects.all())
    network_security_group = serializers.PrimaryKeyRelatedField(queryset=NetworkSecurityGroup.objects.all())
    storage = serializers.PrimaryKeyRelatedField(queryset=Storage.objects.all())


    class Meta:
        model = VirtualMachine
        fields = ['id', 'name', 'public_ip', 'subnet', 'network_security_group', 'storage']


class VirtualMachineRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = VirtualMachine
        fields = ['id', 'name', 'subscription', 'public_ip', 'subnet', 'network_security_group', 'storage']

