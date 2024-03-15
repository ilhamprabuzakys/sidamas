from rest_framework import serializers

from . import models


class Rakernis_psmSerializer(serializers.ModelSerializer):
    dokumentasi = serializers.FileField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = models.rakernis_psm
        fields = [
            "id",
            "id_user",
            "satker_pelaksana",
            "satker_bnnp_bnnk_diundang",
            "deskripsi_hasil",
            "rekomendasi",
            "hambatan_kendala",
            "tanggal",
            "kesimpulan",
            "dokumentasi",
            "created",
            "last_updated",
        ]
