from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import FundInfo
from .serializer import FundInfoSerializer


class FundInfoViewSet(viewsets.ModelViewSet):
    # 声明并实例化，然后生成对象，相当于数据库和模型对象交互的接口
    queryset = FundInfo.objects.all()
    # 序列化的类
    serializer_class = FundInfoSerializer
