from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import task_view_set

router=DefaultRouter() #An instance of DefaultRouter() (from DRF) that auto-generates URLs for viewsets
router.register(r'task',task_view_set) #Please create automatic routes for this TaskViewSet under the URL path /tasks/

urlpatterns=[
    path('',include(router.urls)),
]