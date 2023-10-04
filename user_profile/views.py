from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from .models import UserProfile
from .serializers import UserProfileSerializer  # 이 시리얼라이저는 구현되어 있어야 합니다.

user_profile_pk_parameter = openapi.Parameter(
    'id',
    in_=openapi.IN_PATH,
    description='UUID of the user profile.',
    type=openapi.TYPE_STRING,
    format=openapi.FORMAT_UUID,
    required=True
)


class UserProfileViewSet(mixins.CreateModelMixin,       # 생성
                         mixins.RetrieveModelMixin,     # 단일 항목 검색
                         mixins.ListModelMixin,         # 전체 항목 목록 검색
                         mixins.DestroyModelMixin,      # 삭제
                         viewsets.GenericViewSet):      # 기본 뷰셋 기능 제공

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'  # URL에서 사용할 개별 객체의 키를 지정합니다.

    def retrieve(self, request, *args, **kwargs):
        # 쿼리 파라미터가 있는지 확인
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # 쿼리 파라미터가 있는지 확인
        if request.query_params:
            return Response({"detail": "Query parameters are not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        return super().destroy(request, *args, **kwargs)