from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TPViewSet, MAViewSet, MQViewSet, ACViewSet, search_UserViewSet, SRViewSet, SDViewSet

app_name = 'chat_teesis'

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('thesis-plans', TPViewSet)
router.register('mentor-answers', MAViewSet)
router.register('mentee-questions', MQViewSet)
router.register('answer', ACViewSet)
router.register('search_data',SDViewSet)

urlpatterns = [
    path('search/<slug>/', SRViewSet.as_view(), name="search"),
    path('', include(router.urls)),
    url(r's_users/', search_UserViewSet),
] + router.urls