from django.urls import path, include

from rest_framework import routers

from .views import PostView, LikeView

router = routers.DefaultRouter()
router.register(r'posts', PostView)
router.register(r'likes', LikeView)

urlpatterns = [
    path(r'', include(router.urls)),
]
