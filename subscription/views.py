import uuid

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from .models import Subscription

from rest_framework.generics import get_object_or_404
from user_profile.models import UserProfile
from .serializers import SubscriptionCreateSerializer, SubscriptionListRetrieveSerializer


class SubscriptionViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    queryset = Subscription.objects.all()
    lookup_field = 'id'

    def is_valid_uuid(self, uuid_to_test, version=4):
        try:
            uuid_obj = uuid.UUID(uuid_to_test, version=version)
        except ValueError:
            return False
        return str(uuid_obj) == uuid_to_test

    def get_serializer_class(self):
        if self.action == 'create':
            return SubscriptionCreateSerializer
        return SubscriptionListRetrieveSerializer

    def perform_create(self, serializer):
        user_profile_pk = self.kwargs.get('user_profile_id')
        user_profile = get_object_or_404(UserProfile, id=user_profile_pk)
        serializer.save(user_profile=user_profile)

    def get_queryset(self):
        user_profile_pk = self.kwargs.get('user_profile_id')
        return Subscription.objects.filter(user_profile__id=user_profile_pk)

    @swagger_auto_schema(tags=['subscriptions'], request_body=SubscriptionCreateSerializer)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['subscriptions'])
    def list(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        user_profile_id = self.kwargs.get('user_profile_id')
        if not self.is_valid_uuid(user_profile_id):
            return Response({"detail": "Invalid user_profile_id"}, status=status.HTTP_400_BAD_REQUEST)
        get_object_or_404(UserProfile, id=self.kwargs.get('user_profile_id'))
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['subscriptions'])
    def retrieve(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        user_profile_id = self.kwargs.get('user_profile_id')
        if not self.is_valid_uuid(user_profile_id):
            return Response({"detail": "Invalid user_profile_id"}, status=status.HTTP_400_BAD_REQUEST)
        get_object_or_404(UserProfile, id=self.kwargs.get('user_profile_id'))
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['subscriptions'])
    def destroy(self, request, *args, **kwargs):
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        user_profile_id = self.kwargs.get('user_profile_id')
        if not self.is_valid_uuid(user_profile_id):
            return Response({"detail": "Invalid user_profile_id"}, status=status.HTTP_400_BAD_REQUEST)
        get_object_or_404(UserProfile, id=self.kwargs.get('user_profile_id'))
        return super().destroy(request, *args, **kwargs)
