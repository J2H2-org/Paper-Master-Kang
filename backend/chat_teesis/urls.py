from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TPViewSet, MAViewSet, MQViewSet, CAViewSet, CQViewSet, ACViewSet, search_UserViewSet, \
    SRViewSet, SDViewSet, SIViewSet, SAViewSet, SA2ViewSet

app_name = 'chat_teesis'

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('thesis_plans', TPViewSet)
router.register('mentor_answers', MAViewSet)
router.register('mentee_questions', MQViewSet)
router.register('c_questions', CQViewSet)
router.register('c_answers', CAViewSet)
router.register('answer', ACViewSet)
# router.register('search-data', SDViewSet)

urlpatterns = [
                  path('mentee-questions/search/', SRViewSet.as_view(), name="search"),
                  path('mentee-questions/search/<slug>/', SDViewSet.as_view(), name="search-data"),
                  path('mentee-questions/search/ID/<slug>/', SIViewSet.as_view(), name="search-data"),
                  path('answer/search/', SA2ViewSet.as_view(), name="search-answer"),
                  path('answer/search/<slug>/', SAViewSet.as_view(), name="search-answer"),
                  url(r's_users/<slug:user_Id>/', search_UserViewSet),
              ] + router.urls
