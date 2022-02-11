from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TPViewSet, MAViewSet, MQViewSet, ACViewSet, search_UserViewSet, SRViewSet, SDViewSet

app_name = 'chat_teesis'

router = DefaultRouter()
router.register('/users', UserViewSet)
router.register('/plans', TPViewSet)
router.register('/answers/mento', MAViewSet)
router.register('/questions', MQViewSet)
router.register('/answers/tables', ACViewSet)

urlpatterns = [
    path('search/<slug>/', SRViewSet.as_view(), name="search"),
    path('', include(router.urls)),
    url(r'users/', search_UserViewSet),
] + router.urls
                  