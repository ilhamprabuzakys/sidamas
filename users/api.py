from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from . import serializers
from . import models

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['put'])
    def update_is_staff(self, request, pk=None):
        try:
            profile = self.get_object()
            user = profile.user
            user.is_staff = True
            user.save()

            profile.is_verified = True
            profile.save()
            
            return Response({'detail': 'is_staff updated successfully.'}, status=status.HTTP_200_OK)
        except models.Profile.DoesNotExist:
            return Response({'detail': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)