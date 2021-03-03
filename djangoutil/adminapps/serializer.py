# -*- coding:utf-8 -*-
# @author: 某小健
# @file: serializer.py
# @time: 2021/2/25 23:38
# @desc:
from rest_framework import serializers

from adminapps.models import SubMenu, Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class SubMenuSerializer(serializers.ModelSerializer):
    # 外键查询对应的值，一定要放在Meta外面
    parentMenuName = serializers.ReadOnlyField(source='parentMenu.menuName')

    class Meta:
        model = SubMenu
        fields = '__all__'
