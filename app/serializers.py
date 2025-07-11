from rest_framework import serializers
from .models import taskManager

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=taskManager
        fields='__all__' #include all fields of the model
