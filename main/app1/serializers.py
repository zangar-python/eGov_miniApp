from .models import Messages,Queue
from rest_framework.serializers import ModelSerializer

class MessageSerializer(ModelSerializer):
    class Meta:
        model=Messages
        fields="__all__"

class QueueSerializer(ModelSerializer):
    class Meta:
        model=Queue
        fields="__all__"
