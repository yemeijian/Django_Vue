from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import FundInfo
from .serializer import FundInfoSerializer


class FundInfoViewSet(viewsets.ModelViewSet):
    queryset = FundInfo.objects.all()
    serializer_class = FundInfoSerializer
