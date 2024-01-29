from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
# router.register("tbl_responden_survei", api.tbl_responden_surveiViewSet)
# router.register("tbl_survei", api.tbl_surveiViewSet)
router.register("tbl_data_responden", api.tbl_data_respondenViewSet)
router.register("tbl_isi_survei", api.tbl_isi_surveiViewSet)
router.register("tbl_data_survei", api.tbl_data_surveiViewSet)

# percobaan
router.register("tipe_survei", api.TipeSurveiViewSet)
router.register("data_survei", api.DataSurveiViewSet)
router.register("data_responden_survei", api.DataRespondenSurveiViewSet)
router.register("data_pengisian_survei", api.DataPengisianSurveiViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path(
        "survei/tbl_responden_survei/",
        views.tbl_responden_surveiListView.as_view(),
        name="survei_tbl_responden_survei_list",
    ),
    path(
        "survei/tbl_responden_survei/create/",
        views.tbl_responden_surveiCreateView.as_view(),
        name="survei_tbl_responden_survei_create",
    ),
    path(
        "survei/tbl_responden_survei/detail/<int:pk>/",
        views.tbl_responden_surveiDetailView.as_view(),
        name="survei_tbl_responden_survei_detail",
    ),
    path(
        "survei/tbl_responden_survei/update/<int:pk>/",
        views.tbl_responden_surveiUpdateView.as_view(),
        name="survei_tbl_responden_survei_update",
    ),
    path(
        "survei/tbl_responden_survei/delete/<int:pk>/",
        views.tbl_responden_surveiDeleteView.as_view(),
        name="survei_tbl_responden_survei_delete",
    ),
    path(
        "survei/tbl_survei/",
        views.tbl_surveiListView.as_view(),
        name="survei_tbl_survei_list",
    ),
    path(
        "survei/tbl_survei/create/",
        views.tbl_surveiCreateView.as_view(),
        name="survei_tbl_survei_create",
    ),
    path(
        "survei/tbl_survei/detail/<int:pk>/",
        views.tbl_surveiDetailView.as_view(),
        name="survei_tbl_survei_detail",
    ),
    path(
        "survei/tbl_survei/update/<int:pk>/",
        views.tbl_surveiUpdateView.as_view(),
        name="survei_tbl_survei_update",
    ),
    path(
        "survei/tbl_survei/delete/<int:pk>/",
        views.tbl_surveiDeleteView.as_view(),
        name="survei_tbl_survei_delete",
    ),
)
