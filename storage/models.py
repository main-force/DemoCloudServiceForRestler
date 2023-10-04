from django.db import models
import uuid

from storage_account.models import StorageAccount


class Storage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    storage_account = models.ForeignKey(StorageAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.name[:50]


class Container(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name[:50]


class Blob(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)

    def __str__(self):
        return self.name[:50]
