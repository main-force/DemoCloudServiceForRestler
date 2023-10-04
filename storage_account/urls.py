from rest_framework_nested import routers
from subscription.urls import subscription_router  # Ensure you import the parent router
from .views import StorageAccountViewSet

# Subscription에 nested된 router 정의
storage_account_router = routers.NestedSimpleRouter(subscription_router, r'subscriptions', lookup='subscription', trailing_slash=False)
storage_account_router.register(r'storage-accounts', StorageAccountViewSet, basename='storage-account')
