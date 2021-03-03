# -*- coding:utf-8 -*-
# @author: 某小健
# @file: urls.py
# @time: 2021/2/26 0:24
# @desc:
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from adminapps import views

# router = DefaultRouter()
# router.register(prefix='menu', viewset=views.SubMenuView)  # prefix：接口前缀，viewset：视图集ViewSet
urlpatterns = [
    path('menu/', views.SubMenuView.as_view())
]
