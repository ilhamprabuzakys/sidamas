from django.urls import include, path
from rest_framework import routers
from django.contrib.auth.decorators import login_required

from . import views
from . import api

router = routers.DefaultRouter()
# router.register("update-profile-information", api.UpdateProfileInformationViewSet, basename='update-profile-information')
router.register("update_profile", api.UpdateProfileInformationViewSet)


app_name = 'dashboard'

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("", login_required(views.DashboardView.as_view()), name="index"),
    path("profile/", views.ProfilView.as_view(), name="profile"),
)
