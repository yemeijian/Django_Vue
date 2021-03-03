from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from adminapps.models import SubMenu, Menu
from .serializer import SubMenuSerializer
import logging

# 实例化logging对象,并以当前文件的名字作为logger实例的名字
logger = logging.getLogger(__name__)


# 生成一个名字叫做 collect 的日志实例
# logger_c = logging.getLogger('collect')


class SubMenuView(APIView):
    def get(self, requset):
        # # 声明并实例化，然后生成对象，相当于数据库和模型对象交互的接口
        # queryset = SubMenu.objects.all()
        # # 序列化的类
        # serializer_class = SubMenuSerializer
        menuJson = {}
        menuQuery = SubMenu.objects.all()
        result = SubMenuSerializer(instance=menuQuery, many=True)
        logger.debug(result.data)
        for i in result.data:
            parentMenuId = i['parentMenu']
            if parentMenuId is None:
                continue
            if parentMenuId not in menuJson:
                menuJson[parentMenuId] = {
                    'parentMenuName': i['parentMenuName'],
                    'subMenuList': [
                        {
                            'subMenuName': i['subMenuName'],
                            'subMenuUrl': i['subMenuUrl'],
                            'subMenuShow': i['subMenuShow']
                        }
                    ]
                }
            else:
                menuJson[parentMenuId]['subMenuList'].append(
                    {
                        'subMenuName': i['subMenuName'],
                        'subMenuUrl': i['subMenuUrl'],
                        'subMenuShow': i['subMenuShow']
                    }
                )

        return Response(menuJson, status=status.HTTP_200_OK)

