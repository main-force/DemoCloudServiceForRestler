from django.db import models
import uuid
from subscription.models import Subscription
from public_ip.models import PublicIP


class Subnet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    public_ip = models.ForeignKey(PublicIP, on_delete=models.CASCADE)

    def __str__(self):
        return self.name[:50]
