from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .apps import SalesConfig
from .views import AdViewSet, CommentViewSet



app_name = SalesConfig.name

router = SimpleRouter()
router.register(r'ads', AdViewSet, basename='ads')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'ads/(?P<ad_pk>\d+)/comments', CommentViewSet, basename='comment')



urlpatterns = [
    path("", include(router.urls))
]
