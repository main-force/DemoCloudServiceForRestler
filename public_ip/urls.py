from rest_framework_nested import routers

from subscription.urls import subscription_router
from .views import PublicIPViewSet


public_ip_router = routers.NestedSimpleRouter(subscription_router, r'subscriptions', lookup='subscription', trailing_slash=False)
public_ip_router.register(r'public-ips', PublicIPViewSet, basename='public_ip')
