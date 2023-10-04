from rest_framework_nested import routers

from public_ip.urls import public_ip_router
from .views import SubnetViewSet

# PublicIP에 nested된 router 정의
subnet_router = routers.NestedSimpleRouter(public_ip_router, r'public-ips', lookup='public_ip', trailing_slash=False)
subnet_router.register(r'subnets', SubnetViewSet, basename='subnet')