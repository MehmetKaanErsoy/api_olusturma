from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Urun
import PyQt5
from .serializers import UrunSeri


# Create your views here.

class UrunView(APIView):
    def get(self, request):
        urun_data = Urun.objects.all()
        urun_serial = UrunSeri(urun_data, many=True)
        return Response(urun_serial.data)

    def post(self):
        pass
