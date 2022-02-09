from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TPViewSet, MAViewSet, MQViewSet, CAViewSet, CQViewSet, ACViewSet, search_UserViewSet

app_name = 'chat_teesis'

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('thesis_plans', TPViewSet)
router.register('mentor_answers', MAViewSet)
router.register('mentee_questions', MQViewSet)
router.register('c_questions', CQViewSet)
router.register('c_answers', CAViewSet)
router.register('answer', ACViewSet)

urlpatterns = [
                  url(r's_users/<slug:user_Id>/', search_UserViewSet),
              ] + router.urls
