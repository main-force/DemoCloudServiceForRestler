import uuid

from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from subscription.models import Subscription
from public_ip.models import PublicIP
from .models import Subnet
from .serializers import SubnetSerializer, SubnetCreateSerializer


class SubnetViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    queryset = Subnet.objects.all()
    lookup_field = 'id'

    def is_valid_uuid(self, uuid_to_test, version=4):
        try:
            uuid_obj = uuid.UUID(uuid_to_test, version=version)
        except ValueError:
            return False
        return str(uuid_obj) == uuid_to_test

    def get_serializer_class(self):
        if self.action == 'create':
            return SubnetCreateSerializer
        return SubnetSerializer

    def get_queryset(self):
        public_ip_id = self.kwargs.get('public_ip_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')
        if public_ip_id and subscription_id and user_profile_id:
            subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
            public_ip = get_object_or_404(PublicIP, subscription=subscription, id=public_ip_id)
            return Subnet.objects.filter(public_ip=public_ip)
        return Subnet.objects.none()

    def perform_create(self, serializer):
        public_ip_id = self.kwargs.get('public_ip_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')
        subscription = get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        public_ip = get_object_or_404(PublicIP, subscription=subscription, id=public_ip_id)
        serializer.save(subscription=subscription, public_ip=public_ip)

    @swagger_auto_schema(tags=['subnets'], request_body=SubnetCreateSerializer)
    def create(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        public_ip_id = self.kwargs.get('public_ip_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                public_ip_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['subnets'])
    def list(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        public_ip_id = self.kwargs.get('public_ip_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                public_ip_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['subnets'])
    def retrieve(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        public_ip_id = self.kwargs.get('public_ip_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                public_ip_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        get_object_or_404(PublicIP, subscription__id=subscription_id,
                          id=public_ip_id)
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['subnets'])
    def destroy(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        public_ip_id = self.kwargs.get('public_ip_id')
        subscription_id = self.kwargs.get('subscription_id')
        user_profile_id = self.kwargs.get('user_profile_id')

        if not self.is_valid_uuid(subscription_id) or not self.is_valid_uuid(user_profile_id) or not self.is_valid_uuid(
                public_ip_id):
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        get_object_or_404(Subscription, user_profile=user_profile_id, id=subscription_id)
        get_object_or_404(PublicIP, subscription__id=subscription_id,
                          id=public_ip_id)
        return super().destroy(request, *args, **kwargs)
