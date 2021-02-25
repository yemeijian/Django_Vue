# -*- coding:utf-8 -*-
# @author: 某小健
# @file: serializer.py
# @time: 2021/2/25 23:38
# @desc:
from rest_framework import serializers

from adminapps.models import SubMenu


class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = '__all__'
