from rest_framework import serializers

from apiapps.models import FundInfo


class FundInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundInfo
        fields = '__all__'
