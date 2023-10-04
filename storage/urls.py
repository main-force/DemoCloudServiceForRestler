# urls.py
from rest_framework_nested import routers
from .views import StorageViewSet, ContainerViewSet, BlobViewSet
from storage_account.urls import storage_account_router  # storage_account_router가 정의된 곳에서 가져와야 합니다.

storage_router = routers.NestedSimpleRouter(storage_account_router, r'storage-accounts', lookup='storage_account', trailing_slash=False)
storage_router.register(r'storages', StorageViewSet, basename='storage')

container_router = routers.NestedSimpleRouter(storage_router, r'storages', lookup='storage', trailing_slash=False)
container_router.register(r'containers', ContainerViewSet, basename='container')

blob_router = routers.NestedSimpleRouter(container_router, r'containers', lookup='container', trailing_slash=False)
blob_router.register(r'blobs', BlobViewSet, basename='blob')
