from django.db import models
import uuid

from network_security.models import NetworkSecurityGroup
from public_ip.models import PublicIP
from storage.models import Storage
from subnet.models import Subnet
from subscription.models import Subscription


class VirtualMachine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    public_ip = models.ForeignKey(PublicIP, on_delete=models.CASCADE)
    subnet = models.ForeignKey(Subnet, on_delete=models.CASCADE)
    network_security_group = models.ForeignKey(NetworkSecurityGroup, on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name[:50]
