from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .apps import SalesConfig
from .views import AdViewSet, CommentViewSet

# TODO настройка роутов для модели

app_name = SalesConfig.name

router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ads')
router.register(r'ads/(?P<ad_pk>\d+)/comments', CommentViewSet, basename='comment')

urlpatterns = [
    path("", include(router.urls))
]
