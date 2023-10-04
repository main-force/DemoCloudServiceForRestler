import uuid

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import VirtualMachine
from .serializers import VirtualMachineCreateSerializer, VirtualMachineRetrieveSerializer
from subscription.models import Subscription


class VirtualMachineViewSet(mixins.CreateModelMixin,
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
            return VirtualMachineCreateSerializer
        return VirtualMachineRetrieveSerializer

    def get_queryset(self):
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        # 여기서 user_profile_id와 subscription_id를 활용하여 해  당 Subscription이 존재하는지 확인합니다.
        subscription = get_object_or_404(Subscription, id=subscription_id, user_profile_id=user_profile_id)

        return VirtualMachine.objects.filter(subscription=subscription)

    def perform_create(self, serializer):
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        # 여기서도 user_profile_id와 subscription_id를 활용하여 해당 Subscription이 존재하는지 확인합니다.
        subscription = get_object_or_404(Subscription, id=subscription_id, user_profile_id=user_profile_id)

        serializer.save(subscription=subscription)

    @swagger_auto_schema(tags=['virtual-machines'], request_body=VirtualMachineCreateSerializer)
    def create(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['virtual-machines'])
    def list(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, id=subscription_id, user_profile_id=user_profile_id)
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['virtual-machines'])
    def retrieve(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, id=subscription_id, user_profile_id=user_profile_id)
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['virtual-machines'])
    def destroy(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, id=subscription_id, user_profile_id=user_profile_id)
        return super().destroy(request, *args, **kwargs)
