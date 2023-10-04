import uuid

from rest_framework import mixins, viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from subscription.models import Subscription
from .models import NetworkSecurityGroup, NetworkSecurityPolicy
from .serializers import (
    NetworkSecurityGroupCreateSerializer, NetworkSecurityGroupListRetrieveSerializer,
    NetworkSecurityPolicyCreateSerializer, NetworkSecurityPolicyListRetrieveSerializer
)
from drf_yasg.utils import swagger_auto_schema


class NetworkSecurityGroupViewSet(mixins.CreateModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.ListModelMixin,
                                  mixins.DestroyModelMixin,
                                  viewsets.GenericViewSet):
    queryset = NetworkSecurityGroup.objects.all()
    lookup_field = 'id'

    def is_valid_uuid(self, uuid_to_test, version=4):
        try:
            uuid_obj = uuid.UUID(uuid_to_test, version=version)
        except ValueError:
            return False
        return str(uuid_obj) == uuid_to_test

    def get_serializer_class(self):
        if self.action == 'create':
            return NetworkSecurityGroupCreateSerializer
        return NetworkSecurityGroupListRetrieveSerializer

    def get_queryset(self):
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')
        if subscription_id and user_profile_id:
            if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
                return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

            subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
            return NetworkSecurityGroup.objects.filter(subscription_id=subscription)
        return NetworkSecurityGroup.objects.none()

    def perform_create(self, serializer):
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')
        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        serializer.save(subscription=subscription)

    @swagger_auto_schema(tags=['network-security-groups'])
    def list(self, request, *args, **kwargs):
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['network-security-groups'], request_body=NetworkSecurityGroupCreateSerializer)
    def create(self, request, *args, **kwargs):
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')
        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['network-security-groups'])
    def retrieve(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['network-security-groups'])
    def destroy(self, request, *args, **kwargs):
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)

        return super().destroy(request, *args, **kwargs)


class NetworkSecurityPolicyViewSet(mixins.CreateModelMixin,
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
            return NetworkSecurityPolicyCreateSerializer
        return NetworkSecurityPolicyListRetrieveSerializer

    def get_queryset(self):
        network_security_group_id = self.kwargs.get('network_security_group_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(network_security_group_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)
        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        group = get_object_or_404(NetworkSecurityGroup, id=network_security_group_id, subscription=subscription)
        return NetworkSecurityPolicy.objects.filter(network_security_group_id=group)

    def perform_create(self, serializer):
        network_security_group_id = self.kwargs.get('network_security_group_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                network_security_group_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)
        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        group = get_object_or_404(NetworkSecurityGroup, id=network_security_group_id, subscription=subscription)
        serializer.save(network_security_group=group)

    @swagger_auto_schema(tags=['network-security-policies'], request_body=NetworkSecurityPolicyCreateSerializer)
    def create(self, request, *args, **kwargs):
        network_security_group_id = self.kwargs.get('network_security_group_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                network_security_group_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['network-security-policies'])
    def list(self, request, *args, **kwargs):
        network_security_group_id = self.kwargs.get('network_security_group_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                network_security_group_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        get_object_or_404(NetworkSecurityGroup, id=network_security_group_id, subscription=subscription)

        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['network-security-policies'])
    def retrieve(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        network_security_group_id = self.kwargs.get('network_security_group_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                network_security_group_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)
        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        get_object_or_404(NetworkSecurityGroup, id=network_security_group_id, subscription=subscription)

        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['network-security-policies'])
    def destroy(self, request, *args, **kwargs):
        network_security_group_id = self.kwargs.get('network_security_group_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                network_security_group_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)
        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        get_object_or_404(NetworkSecurityGroup, id=network_security_group_id, subscription=subscription)

        return super().destroy(request, *args, **kwargs)
