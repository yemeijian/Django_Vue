import os
import random

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FundInfo
from .serializer import FundInfoSerializer


class FundInfoViewSet(viewsets.ModelViewSet):
    # 声明并实例化，然后生成对象，相当于数据库和模型对象交互的接口
    queryset = FundInfo.objects.all()
    # 序列化的类
    serializer_class = FundInfoSerializer


class RandomImage(APIView):
    def get(self, requset):
        imageList = []
        for fileName in os.listdir(
                os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'media')):
            if fileName.endswith('jpg') or fileName.endswith('png'):
                imageList.append(fileName)
        return Response(requset.path + '/' + random.choice(imageList), status=status.HTTP_200_OK)
