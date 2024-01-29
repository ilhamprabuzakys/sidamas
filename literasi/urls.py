from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("literasi", api.LiterasiViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("", views.LiterasiView.as_view(), name="literasi"),
    path("literasi/", views.LiterasiListView.as_view(), name="literasi_literasi_list"),
    path("literasi/create/", views.LiterasiCreateView.as_view(), name="literasi_literasi_create"),
    path("literasi/detail/<int:pk>/", views.LiterasiDetailView.as_view(), name="literasi_literasi_detail"),
    path("literasi/update/<int:pk>/", views.LiterasiUpdateView.as_view(), name="literasi_literasi_update"),
    path("literasi/delete/<int:pk>/", views.LiterasiDeleteView.as_view(), name="literasi_literasi_delete"),
)
