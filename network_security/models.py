from django.db import models
import uuid
from subscription.models import Subscription


class NetworkSecurityGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return self.name[:50]


class NetworkSecurityPolicy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    network_security_group = models.ForeignKey(NetworkSecurityGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name[:50]

