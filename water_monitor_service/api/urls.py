from rest_framework import routers
from django.urls import path, include

from api.views import WaterMonitoringViewSet


router = routers.DefaultRouter()
router.register(r"water-monitoring", WaterMonitoringViewSet)

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
]