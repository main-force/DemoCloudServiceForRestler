# serializers.py
from rest_framework import serializers
from .models import Storage, Container, Blob


class StorageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['id', 'name']  # storage_account를 포함하여야 ForeignKey로 설정되어있기 때문입니다.


class StorageListRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = ['id', 'name', 'storage_account']


class ContainerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = ['id', 'name']  # storage를 포함하여야 ForeignKey로 설정되어있기 때문입니다.


class ContainerListRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Container
        fields = ['id', 'name', 'storage']


class BlobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blob
        fields = ['id', 'name']  # container를 포함하여야 ForeignKey로 설정되어있기 때문입니다.


class BlobListRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blob
        fields = ['id', 'name', 'container']
