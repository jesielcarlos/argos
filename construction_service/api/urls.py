from rest_framework import routers
from django.urls import path, include

from api.views import ProjectViewSet


router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet)

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
]