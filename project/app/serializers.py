from rest_framework import serializers
from app.models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = MyModel
        fields = '__all__'
