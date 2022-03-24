from rest_framework import serializers
from proje.models import Urun


class UrunSeri(serializers.ModelSerializer):
    class Meta:
        model = Urun
        fields = '__all__'
