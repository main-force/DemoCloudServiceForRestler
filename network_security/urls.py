from rest_framework_nested import routers
from .views import NetworkSecurityGroupViewSet, NetworkSecurityPolicyViewSet
from subscription.urls import subscription_router  # subscription_router가 정의된 곳에서 가져와야 합니다.

# NetworkSecurityGroup를 Subscription의 nested router로 등록
network_security_group_router = routers.NestedSimpleRouter(subscription_router, r'subscriptions', lookup='subscription', trailing_slash=False)
network_security_group_router.register(r'network-security-groups', NetworkSecurityGroupViewSet, basename='network_security_group')

# NetworkSecurityPolicy를 NetworkSecurityGroup의 nested router로 등록
network_security_policy_router = routers.NestedSimpleRouter(network_security_group_router, r'network-security-groups', lookup='network_security_group', trailing_slash=False)
network_security_policy_router.register(r'policies', NetworkSecurityPolicyViewSet, basename='network_security_policy')
