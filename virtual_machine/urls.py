from rest_framework_nested import routers

from subscription.urls import subscription_router
from .views import VirtualMachineViewSet

virtual_machine_router = routers.NestedSimpleRouter(subscription_router, r'subscriptions', lookup='subscription', trailing_slash=False)
virtual_machine_router.register(r'virtual-machines', VirtualMachineViewSet, basename='virtual_machine')
