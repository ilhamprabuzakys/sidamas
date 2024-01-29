from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
# percobaan
router.register("tipe_survei", api.TipeSurveiViewSet)
router.register("data_survei", api.DataSurveiViewSet)
router.register("data_responden_survei", api.DataRespondenSurveiViewSet)
router.register("data_pengisian_survei", api.DataPengisianSurveiViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
)
