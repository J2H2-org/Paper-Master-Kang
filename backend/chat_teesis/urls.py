from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TPViewSet, MAViewSet, MQViewSet, SRViewSet, SDViewSet, SIViewSet, SAViewSet, SA2ViewSet, SearchQtoAViewSet, MAIViewSet, UAViewSet, UQViewSet

app_name = 'chat_teesis'

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('plans', TPViewSet)
router.register('answers', MAViewSet)
router.register('questions', MQViewSet)

urlpatterns = [
    path('questions/search/', SRViewSet.as_view(), name="search_m/s"),
    path('questions/search/key/<search_word>/', SDViewSet.as_view(), name="search-m/s"),
    path('questions/search/id/<mentee_question_Id>/', SIViewSet.as_view(), name="search-data"),
    path('questions/search/id/<user_Id>/', UQViewSet.as_view(), name="user_Id"),
    path('answers/search/', SA2ViewSet.as_view(), name="search-answer"),
    path('answers/search/<search_word>/', SAViewSet.as_view(), name="search-answer"),
    path('answers/search/id/<mentee_question_Id>/', MAIViewSet.as_view(), name="question_ID"),
    path('answers/search/id/<user_Id>/', UAViewSet.as_view(), name="user_ID"),

] + router.urls
