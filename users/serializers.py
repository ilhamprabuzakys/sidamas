from rest_framework import serializers
from django.contrib.auth.models import User

from . import models

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = [
            "id",
            "avatar",
            "user",
            "role",
            "satker",
            "is_verified",
        ]

class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_staff']