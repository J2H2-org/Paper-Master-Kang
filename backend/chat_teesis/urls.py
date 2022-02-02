from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TPViewSet, MAViewSet, MQViewSet

app_name = 'chat_teesis'

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('thesis_plans', TPViewSet)
router.register('mentor_answers', MAViewSet)
router.register('mentee_questions', MQViewSet)

urlpatterns = [] + router.urls
