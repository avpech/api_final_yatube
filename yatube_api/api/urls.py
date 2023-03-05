from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from api import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'groups', views.GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)
router.register(r'follow', views.FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
    path(
        'v1/jwt/create/',
        TokenObtainPairView.as_view(),
        name='token_create'
    ),
    path(
        'v1/jwt/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'v1/jwt/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    )
]
