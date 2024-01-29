from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

app_name = "users"

router = routers.DefaultRouter()
router.register("profile", api.ProfileViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("registrasi/", views.RegistrasiUserList.as_view(), name="registrasi_user"),
    path("profile/", views.MyProfile.as_view(), name="index"),
    path("verifikasi/", views.UserVerificationListView.as_view(), name="list_verified"),
]