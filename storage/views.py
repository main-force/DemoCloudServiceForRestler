import uuid

from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from subscription.models import Subscription
from .models import Storage, Container, Blob
from .serializers import (
    StorageCreateSerializer, StorageListRetrieveSerializer,
    ContainerCreateSerializer, ContainerListRetrieveSerializer,
    BlobCreateSerializer, BlobListRetrieveSerializer
)

from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from subscription.models import Subscription
from storage_account.models import StorageAccount  # 알맞게 Import 해주셔야 합니다.
from .models import Storage
from .serializers import StorageCreateSerializer, StorageListRetrieveSerializer


class StorageViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    lookup_field = 'id'

    def is_valid_uuid(self, uuid_to_test, version=4):
        try:
            uuid_obj = uuid.UUID(uuid_to_test, version=version)
        except ValueError:
            return False
        return str(uuid_obj) == uuid_to_test

    def get_serializer_class(self):
        if self.action == 'create':
            return StorageCreateSerializer
        return StorageListRetrieveSerializer

    def get_queryset(self):
        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        # 상위 계층 객체들이 존재하는지 확인
        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        get_object_or_404(StorageAccount, id=storage_account_id, subscription=subscription)

        return Storage.objects.filter(storage_account_id=storage_account_id)

    def perform_create(self, serializer):
        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        # 상위 계층 객체들이 존재하는지 확인
        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        storage_account = get_object_or_404(StorageAccount, id=storage_account_id, subscription=subscription)

        serializer.save(storage_account=storage_account)

    @swagger_auto_schema(tags=['storages'], request_body=StorageCreateSerializer)
    def create(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                storage_account_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['storages'])
    def list(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                storage_account_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['storages'])
    def retrieve(self, request, *args, **kwargs):
        # 필요한 경우 여기에서도 상위 계층 객체 확인 가능
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                storage_account_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, id=self.kwargs.get('subscription_id'), user_profile=self.kwargs.get('user_profile_id'))
        get_object_or_404(StorageAccount, id=self.kwargs.get('storage_account_id'), subscription=self.kwargs.get('subscription_id'))
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['storages'])
    def destroy(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                storage_account_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, id=self.kwargs.get('subscription_id'), user_profile=self.kwargs.get('user_profile_id'))
        get_object_or_404(StorageAccount, id=self.kwargs.get('storage_account_id'), subscription=self.kwargs.get('subscription_id'))
        return super().destroy(request, *args, **kwargs)


class ContainerViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    lookup_field = 'id'

    def is_valid_uuid(self, uuid_to_test, version=4):
        try:
            uuid_obj = uuid.UUID(uuid_to_test, version=version)
        except ValueError:
            return False
        return str(uuid_obj) == uuid_to_test

    def get_serializer_class(self):
        if self.action == 'create':
            return ContainerCreateSerializer
        return ContainerListRetrieveSerializer

    def get_queryset(self):
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')
        storage_account_id = self.kwargs.get('storage_account_id')
        storage_id = self.kwargs.get('storage_id')

        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        storage_account = get_object_or_404(StorageAccount, subscription=subscription, id=storage_account_id)
        storage = get_object_or_404(Storage, storage_account=storage_account, id=storage_id)

        return Container.objects.filter(storage=storage)

    def perform_create(self, serializer):
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')
        storage_account_id = self.kwargs.get('storage_account_id')
        storage_id = self.kwargs.get('storage_id')

        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        storage_account = get_object_or_404(StorageAccount, subscription=subscription, id=storage_account_id)
        storage = get_object_or_404(Storage, storage_account=storage_account, id=storage_id)

        serializer.save(storage=storage)

    @swagger_auto_schema(tags=['containers'], request_body=ContainerCreateSerializer)
    def create(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        storage_id = self.kwargs.get('storage_id')
        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                storage_account_id) or not self.is_valid_uuid(storage_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['containers'])
    def list(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        storage_id = self.kwargs.get('storage_id')
        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                storage_account_id) or not self.is_valid_uuid(storage_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['containers'])
    def retrieve(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        storage_id = self.kwargs.get('storage_id')
        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                storage_account_id) or not self.is_valid_uuid(storage_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, id=subscription_id, user_profile=user_profile_id)
        get_object_or_404(StorageAccount, id=storage_account_id, subscription=subscription_id)
        get_object_or_404(Storage, id=storage_id, storage_account=storage_account_id)

        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['containers'])
    def destroy(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        storage_id = self.kwargs.get('storage_id')
        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                storage_account_id) or not self.is_valid_uuid(storage_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, id=subscription_id, user_profile=user_profile_id)
        get_object_or_404(StorageAccount, id=storage_account_id, subscription=subscription_id)
        get_object_or_404(Storage, id=storage_id, storage_account=storage_account_id)

        return super().destroy(request, *args, **kwargs)


class BlobViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    lookup_field = 'id'

    def is_valid_uuid(self, uuid_to_test, version=4):
        try:
            uuid_obj = uuid.UUID(uuid_to_test, version=version)
        except ValueError:
            return False
        return str(uuid_obj) == uuid_to_test

    def get_serializer_class(self):
        if self.action == 'create':
            return BlobCreateSerializer
        return BlobListRetrieveSerializer

    def get_queryset(self):
        container_id = self.kwargs.get('container_id')
        storage_id = self.kwargs.get('storage_id')
        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        storage_account = get_object_or_404(StorageAccount, subscription=subscription, id=storage_account_id)
        storage = get_object_or_404(Storage, storage_account=storage_account, id=storage_id)
        container = get_object_or_404(Container, storage=storage, id=container_id)

        return Blob.objects.filter(container=container)

    def perform_create(self, serializer):
        container_id = self.kwargs.get('container_id')
        storage_id = self.kwargs.get('storage_id')
        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        storage_account = get_object_or_404(StorageAccount, subscription=subscription, id=storage_account_id)
        storage = get_object_or_404(Storage, storage_account=storage_account, id=storage_id)
        container = get_object_or_404(Container, storage=storage, id=container_id)

        serializer.save(container=container)

    @swagger_auto_schema(tags=['blobs'], request_body=BlobCreateSerializer)
    def create(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        container_id = self.kwargs.get('container_id')
        storage_id = self.kwargs.get('storage_id')
        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(storage_account_id) or not self.is_valid_uuid(storage_id) or not self.is_valid_uuid(container_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['blobs'])
    def list(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        container_id = self.kwargs.get('container_id')
        storage_id = self.kwargs.get('storage_id')
        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                storage_account_id) or not self.is_valid_uuid(storage_id) or not self.is_valid_uuid(container_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['blobs'])
    def retrieve(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        container_id = self.kwargs.get('container_id')
        storage_id = self.kwargs.get('storage_id')
        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                storage_account_id) or not self.is_valid_uuid(storage_id) or not self.is_valid_uuid(container_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        get_object_or_404(StorageAccount, id=storage_account_id, subscription=subscription_id)
        get_object_or_404(Storage, id=storage_id, storage_account=storage_account_id)
        get_object_or_404(Container, id=container_id, storage_id=storage_id)

        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['blobs'])
    def destroy(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        container_id = self.kwargs.get('container_id')
        storage_id = self.kwargs.get('storage_id')
        storage_account_id = self.kwargs.get('storage_account_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                storage_account_id) or not self.is_valid_uuid(storage_id) or not self.is_valid_uuid(container_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        get_object_or_404(StorageAccount, id=storage_account_id, subscription=subscription_id)
        get_object_or_404(Storage, id=storage_id, storage_account=storage_account_id)
        get_object_or_404(Container, id=container_id, storage_id=storage_id)

        return super().destroy(request, *args, **kwargs)
