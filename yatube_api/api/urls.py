from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register('api/v1/posts', PostViewSet)
router.register('api/v1/groups', GroupViewSet)
router.register(r'api/v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename=r'api/v1/posts/(?P<post_id>\d+)/comments')


urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]

# print(router.urls)
