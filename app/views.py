from django.shortcuts import render
from rest_framework import viewsets
from .models import taskManager
from .serializers import TaskSerializer

# The viewset class that handles the logic for GET, POST, PUT, DELETE

class task_view_set(viewsets.ModelViewSet):
    queryset=taskManager.objects.all()
    serializer_class=TaskSerializer

