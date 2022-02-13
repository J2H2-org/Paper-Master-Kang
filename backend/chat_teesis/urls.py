from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TPViewSet, MAViewSet, MQViewSet, SearchQtoAViewSet, SRViewSet

app_name = 'chat_teesis'

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('plans', TPViewSet)
router.register('answers', MAViewSet)
router.register('questions', MQViewSet)

urlpatterns = [
    path('search/<slug>/', SRViewSet.as_view(), name="search"),
    path('', include(router.urls)),
    path('questions/answers/<slug:mentee_question_Id>', SearchQtoAViewSet.as_view())
] + router.urls
                  