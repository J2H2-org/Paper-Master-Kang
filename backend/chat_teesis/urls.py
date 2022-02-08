from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import UserViewSet, TPViewSet, MAViewSet, MQViewSet, CAViewSet, CQViewSet, SRViewSet

app_name = 'chat_teesis'

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('thesis_plans', TPViewSet)
router.register('mentor_answers', MAViewSet)
router.register('mentee_questions', MQViewSet)
router.register('c_questions', CQViewSet)
router.register('c_answers', CAViewSet)

urlpatterns = [
    path('search/<slug>/', SRViewSet.as_view(), name="search"),
    path('', include(router.urls)),
]
