from rest_framework_nested import routers
from .views import SubscriptionViewSet
from user_profile.urls import router as user_profile_router

subscription_router = routers.NestedSimpleRouter(user_profile_router, r'user_profiles', lookup='user_profile', trailing_slash=False)
subscription_router.register(r'subscriptions', SubscriptionViewSet, basename='user_profile-subscription')

