from rest_framework import routers
from django.urls import path, include
from api.views import KPIViewSet


router = routers.DefaultRouter()
router.register(r"kpis", KPIViewSet)

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
]