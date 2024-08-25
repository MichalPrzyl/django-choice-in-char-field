from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.response import Response

from app.models import MyModel
from app.serializers import MyModelSerializer

class MyModelAPI(ListAPIView, UpdateAPIView, CreateAPIView):
    queryset = MyModel.objects
    serializer_class = MyModelSerializer
