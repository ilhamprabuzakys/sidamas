from rest_framework import viewsets, permissions

from . import serializers
from . import models


class tbl_asistensi_pelaksanaan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_asistensi_pelaksanaan_psm class"""

    queryset = models.tbl_asistensi_pelaksanaan_psm.objects.all()
    serializer_class = serializers.tbl_asistensi_pelaksanaan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_asistensi_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_asistensi_psm class"""

    queryset = models.tbl_asistensi_psm.objects.all()
    serializer_class = serializers.tbl_asistensi_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_audiensi_pelaksanaan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_audiensi_pelaksanaan_psm class"""

    queryset = models.tbl_audiensi_pelaksanaan_psm.objects.all()
    serializer_class = serializers.tbl_audiensi_pelaksanaan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_audiensi_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_audiensi_psm class"""

    queryset = models.tbl_audiensi_psm.objects.all()
    serializer_class = serializers.tbl_audiensi_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_bimbingan_teknis_life_skill_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_bimbingan_teknis_life_skill_dayatif class"""

    queryset = models.tbl_bimbingan_teknis_life_skill_dayatif.objects.all()
    serializer_class = serializers.tbl_bimbingan_teknis_life_skill_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_bimbingan_teknis_life_skill_detail_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_bimbingan_teknis_life_skill_detail_dayatif class"""

    queryset = models.tbl_bimbingan_teknis_life_skill_detail_dayatif.objects.all()
    serializer_class = serializers.tbl_bimbingan_teknis_life_skill_detail_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_bimtek_penggiat_p4gn_lingkungan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_bimtek_penggiat_p4gn_lingkungan_psm class"""

    queryset = models.tbl_bimtek_penggiat_p4gn_lingkungan_psm.objects.all()
    serializer_class = serializers.tbl_bimtek_penggiat_p4gn_lingkungan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_bimtek_penggiat_p4gn_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_bimtek_penggiat_p4gn_psm class"""

    queryset = models.tbl_bimtek_penggiat_p4gn_psm.objects.all()
    serializer_class = serializers.tbl_bimtek_penggiat_p4gn_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_bimtek_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_bimtek_psm class"""

    queryset = models.tbl_bimtek_psm.objects.all()
    serializer_class = serializers.tbl_bimtek_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psm class"""

    queryset = models.tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psm.objects.all()
    serializer_class = serializers.tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_data_dukungan_stakeholder_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_data_dukungan_stakeholder_psm class"""

    queryset = models.tbl_data_dukungan_stakeholder_psm.objects.all()
    serializer_class = serializers.tbl_data_dukungan_stakeholder_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatif class"""

    queryset = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatif.objects.all()
    serializer_class = serializers.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatif class"""

    queryset = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatif.objects.all()
    serializer_class = serializers.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_kegiatan_bimtek_stakeholder_pendamping_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif class"""

    queryset = models.tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif.objects.all()
    serializer_class = serializers.tbl_kegiatan_bimtek_stakeholder_pendamping_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatif class"""

    queryset = models.tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatif.objects.all()
    serializer_class = serializers.tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_kegiatan_lainnya_pelaksanaan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_kegiatan_lainnya_pelaksanaan_psm class"""

    queryset = models.tbl_kegiatan_lainnya_pelaksanaan_psm.objects.all()
    serializer_class = serializers.tbl_kegiatan_lainnya_pelaksanaan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_kegiatan_lainnya_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_kegiatan_lainnya_psm class"""

    queryset = models.tbl_kegiatan_lainnya_psm.objects.all()
    serializer_class = serializers.tbl_kegiatan_lainnya_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_konsolidasi_kebijakan_pelaksanaan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_konsolidasi_kebijakan_pelaksanaan_psm class"""

    queryset = models.tbl_konsolidasi_kebijakan_pelaksanaan_psm.objects.all()
    serializer_class = serializers.tbl_konsolidasi_kebijakan_pelaksanaan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_konsolidasi_kebijakan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_konsolidasi_kebijakan_psm class"""

    queryset = models.tbl_konsolidasi_kebijakan_psm.objects.all()
    serializer_class = serializers.tbl_konsolidasi_kebijakan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatif class"""

    queryset = models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatif.objects.all()
    serializer_class = serializers.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatif class"""

    queryset = models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatif.objects.all()
    serializer_class = serializers.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_monev_rangka_pendampingan_masyarakat_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_monev_rangka_pendampingan_masyarakat_dayatif class"""

    queryset = models.tbl_monev_rangka_pendampingan_masyarakat_dayatif.objects.all()
    serializer_class = serializers.tbl_monev_rangka_pendampingan_masyarakat_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_monev_rangka_pendampingan_masyarakat_detail_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_monev_rangka_pendampingan_masyarakat_detail_dayatif class"""

    queryset = models.tbl_monev_rangka_pendampingan_masyarakat_detail_dayatif.objects.all()
    serializer_class = serializers.tbl_monev_rangka_pendampingan_masyarakat_detail_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psm class"""

    queryset = models.tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psm.objects.all()
    serializer_class = serializers.tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_monev_supervisi_kegiatan_kotan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_monev_supervisi_kegiatan_kotan_psm class"""

    queryset = models.tbl_monev_supervisi_kegiatan_kotan_psm.objects.all()
    serializer_class = serializers.tbl_monev_supervisi_kegiatan_kotan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatif class"""

    queryset = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatif.objects.all()
    serializer_class = serializers.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatif class"""

    queryset = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatif.objects.all()
    serializer_class = serializers.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatif class"""

    queryset = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatif.objects.all()
    serializer_class = serializers.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatif class"""

    queryset = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatif.objects.all()
    serializer_class = serializers.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_pengumpulan_data_ikotan_pelaksanaan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_pengumpulan_data_ikotan_pelaksanaan_psm class"""

    queryset = models.tbl_pengumpulan_data_ikotan_pelaksanaan_psm.objects.all()
    serializer_class = serializers.tbl_pengumpulan_data_ikotan_pelaksanaan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_pengumpulan_data_ikotan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_pengumpulan_data_ikotan_psm class"""

    queryset = models.tbl_pengumpulan_data_ikotan_psm.objects.all()
    serializer_class = serializers.tbl_pengumpulan_data_ikotan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_rakernis_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_rakernis_psm class"""

    queryset = models.tbl_rakernis_psm.objects.all()
    serializer_class = serializers.tbl_rakernis_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_rakor_pemetaan_pelaksanaan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_rakor_pemetaan_pelaksanaan_psm class"""

    queryset = models.tbl_rakor_pemetaan_pelaksanaan_psm.objects.all()
    serializer_class = serializers.tbl_rakor_pemetaan_pelaksanaan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_rakor_pemetaan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_rakor_pemetaan_psm class"""

    queryset = models.tbl_rakor_pemetaan_psm.objects.all()
    serializer_class = serializers.tbl_rakor_pemetaan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatif class"""

    queryset = models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatif.objects.all()
    serializer_class = serializers.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatif class"""

    queryset = models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatif.objects.all()
    serializer_class = serializers.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_rekapitulasi_pembinaan_teknis_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_rekapitulasi_pembinaan_teknis_dayatif class"""

    queryset = models.tbl_rekapitulasi_pembinaan_teknis_dayatif.objects.all()
    serializer_class = serializers.tbl_rekapitulasi_pembinaan_teknis_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_rekapitulasi_pembinaan_teknis_detail_dayatifViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_rekapitulasi_pembinaan_teknis_detail_dayatif class"""

    queryset = models.tbl_rekapitulasi_pembinaan_teknis_detail_dayatif.objects.all()
    serializer_class = serializers.tbl_rekapitulasi_pembinaan_teknis_detail_dayatifSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_sinkronisasi_kebijakan_pelaksanaan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_sinkronisasi_kebijakan_pelaksanaan_psm class"""

    queryset = models.tbl_sinkronisasi_kebijakan_pelaksanaan_psm.objects.all()
    serializer_class = serializers.tbl_sinkronisasi_kebijakan_pelaksanaan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_sinkronisasi_kebijakan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_sinkronisasi_kebijakan_psm class"""

    queryset = models.tbl_sinkronisasi_kebijakan_psm.objects.all()
    serializer_class = serializers.tbl_sinkronisasi_kebijakan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_tes_urine_deteksi_dini_pelaksanaan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_tes_urine_deteksi_dini_pelaksanaan_psm class"""

    queryset = models.tbl_tes_urine_deteksi_dini_pelaksanaan_psm.objects.all()
    serializer_class = serializers.tbl_tes_urine_deteksi_dini_pelaksanaan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_tes_urine_deteksi_dini_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_tes_urine_deteksi_dini_psm class"""

    queryset = models.tbl_tes_urine_deteksi_dini_psm.objects.all()
    serializer_class = serializers.tbl_tes_urine_deteksi_dini_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_workshop_penggiat_pelaksanaan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_workshop_penggiat_pelaksanaan_psm class"""

    queryset = models.tbl_workshop_penggiat_pelaksanaan_psm.objects.all()
    serializer_class = serializers.tbl_workshop_penggiat_pelaksanaan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_workshop_penggiat_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_workshop_penggiat_psm class"""

    queryset = models.tbl_workshop_penggiat_psm.objects.all()
    serializer_class = serializers.tbl_workshop_penggiat_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_workshop_tematik_pelaksanaan_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_workshop_tematik_pelaksanaan_psm class"""

    queryset = models.tbl_workshop_tematik_pelaksanaan_psm.objects.all()
    serializer_class = serializers.tbl_workshop_tematik_pelaksanaan_psmSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_workshop_tematik_psmViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_workshop_tematik_psm class"""

    queryset = models.tbl_workshop_tematik_psm.objects.all()
    serializer_class = serializers.tbl_workshop_tematik_psmSerializer
    permission_classes = [permissions.IsAuthenticated]