import uuid

from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from subscription.models import Subscription
from .models import PublicIP
from .serializers import PublicIPRetrieveSerializer, PublicIPCreateSerializer


class PublicIPViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    queryset = PublicIP.objects.all()
    serializer_class = PublicIPRetrieveSerializer
    lookup_field = 'id'

    def is_valid_uuid(self, uuid_to_test, version=4):
        try:
            uuid_obj = uuid.UUID(uuid_to_test, version=version)
        except ValueError:
            return False
        return str(uuid_obj) == uuid_to_test

    def get_serializer_class(self):
        if self.action == 'create':
            return PublicIPCreateSerializer
        return PublicIPRetrieveSerializer

    def get_queryset(self):
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')
        if subscription_id and user_profile_id:
            subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
            return PublicIP.objects.filter(subscription_id=subscription)
        return PublicIP.objects.none()

    def perform_create(self, serializer):
        subcription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')
        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subcription_id)
        serializer.save(subscription=subscription)

    @swagger_auto_schema(tags=['public-ips'])
    def list(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')
        if subscription_id and user_profile_id:
            if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
                return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['public-ips'], request_body=PublicIPCreateSerializer)
    def create(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')
        if subscription_id and user_profile_id:
            if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
                return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['public-ips'])
    def retrieve(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')
        if subscription_id and user_profile_id:
            if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
                return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, user_profile=self.kwargs.get('user_profile_id'),
                          id=self.kwargs.get('subscription_id'))
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['public-ips'])
    def destroy(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')
        if subscription_id and user_profile_id:
            if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id):
                return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, user_profile=self.kwargs.get('user_profile_id'),
                          id=self.kwargs.get('subscription_id'))
        return super().destroy(request, *args, **kwargs)