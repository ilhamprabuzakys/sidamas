from rest_framework import serializers

from . import models


class LiterasiSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Literasi
        fields = [
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "dokumen",
            "Judul",
            "status",
            "kategori",
            "tags",
        ]
