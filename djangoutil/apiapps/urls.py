from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apiapps import views

router = DefaultRouter()
router.register('fundinfo', views.FundInfoViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
