from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apiapps import views
from djangoutil import settings

router = DefaultRouter()
router.register(prefix='fundinfo', viewset=views.FundInfoViewSet)   # prefix：接口前缀，viewset：视图集ViewSet
urlpatterns = [
    path('', include(router.urls)),
    path('randomimage', views.RandomImage.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
