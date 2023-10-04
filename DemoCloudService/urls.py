from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from subnet.urls import subnet_router
from user_profile.urls import router as user_profile_router
from subscription.urls import subscription_router
from network_security.urls import network_security_group_router, network_security_policy_router
from public_ip.urls import public_ip_router
from storage_account.urls import storage_account_router
from storage.urls import storage_router, container_router, blob_router
from virtual_machine.urls import virtual_machine_router


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('', include(user_profile_router.urls)),
    path('', include(subscription_router.urls)),
    path('', include(network_security_group_router.urls)),
    path('', include(network_security_policy_router.urls)),
    path('', include(public_ip_router.urls)),
    path('', include(subnet_router.urls)),
    path('', include(storage_account_router.urls)),
    path('', include(storage_router.urls)),
    path('', include(container_router.urls)),
    path('', include(blob_router.urls)),
    path('', include(virtual_machine_router.urls))
]