from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from adminapps.models import SubMenu, Menu
from .serializer import SubMenuSerializer


class SubMenuViewSet(viewsets.ModelViewSet):
    # 声明并实例化，然后生成对象，相当于数据库和模型对象交互的接口
    queryset = SubMenu.objects.all()
    # 序列化的类
    serializer_class = SubMenuSerializer
