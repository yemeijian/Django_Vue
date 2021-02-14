from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apiapps import views

router = DefaultRouter()
router.register(prefix='fundinfo', viewset=views.FundInfoViewSet)   # prefix：接口前缀，viewset：视图集ViewSet
urlpatterns = [
    path('', include(router.urls)),
]
