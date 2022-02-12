from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TPViewSet, MAViewSet, MQViewSet, CAViewSet, CQViewSet, ACViewSet, search_UserViewSet, \
    SRViewSet, SDViewSet, SIViewSet

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
                  path('mentee_questions/search/', SRViewSet.as_view(), name="search"),
                  path('mentee_questions/search/<slug>/', SDViewSet.as_view(), name="search-data"),
                  path('mentee_questions/search/ID/<slug>/', SIViewSet.as_view(), name="search-data"),
                  url(r's_users/<slug:user_Id>/', search_UserViewSet),
              ] + router.urls
