from rest_framework import serializers

from . import models


class tbl_asistensi_pelaksanaan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_asistensi_pelaksanaan_psm
        fields = [
            "id_tbl_asistensi_psm",
            "no",
            "tanggal",
            "jumlah_peserta",
            "stakeholde_yang_diasistensi_dalam_rangka_kotan",
            "deskripsi_hasil",
            "kendala_hambatan",
            "kesimpulan",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_asistensi_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_asistensi_psm
        fields = [
            "id_user",
            "satuan_kerja",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_audiensi_pelaksanaan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_audiensi_pelaksanaan_psm
        fields = [
            "id_tbl_audiensi_psm",
            "no",
            "tanggal",
            "peserta",
            "sasaran_lingkungan",
            "deskripsi_hasil",
            "hambatan_kendala",
            "kesimpulan",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_audiensi_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_audiensi_psm
        fields = [
            "id_user",
            "satuan_kerja_pelaksana_kegiatan",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_bimbingan_teknis_life_skill_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_bimbingan_teknis_life_skill_dayatif
        fields = [
            "id_user",
            "satuan_kerja",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_bimbingan_teknis_life_skill_detail_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_bimbingan_teknis_life_skill_detail_dayatif
        fields = [
            "id_tbl_bimbingan_teknis_life_skill_dayatif",
            "no",
            "nilai",
            "created",
            "tindak_lanjut",
            "kesimpulan",
            "desa_bersinar",
            "nama_kawasan",
            "tanggal",
            "kategori",
            "nama_peserta",
            "IBM",
            "file",
            "jumlah_peserta",
            "pria",
            "wanita",
            "last_updated",
        ]

class tbl_bimtek_penggiat_p4gn_lingkungan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_bimtek_penggiat_p4gn_lingkungan_psm
        fields = [
            "id_tbl_bimtek_penggiat_p4gn_psm",
            "no",
            "tanggal",
            "nama_lingkungan",
            "no_seri_pin_penggiat",
            "nama",
            "jabatan",
            "jenis_kelamin",
            "jumlah_peserta",
            "daftar_nama_peserta",
            "hasil_capaian",
            "kesimpulan",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_bimtek_penggiat_p4gn_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_bimtek_penggiat_p4gn_psm
        fields = [
            "id_user",
            "satuan_kerja_pelaksana_kegiatan",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_bimtek_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_bimtek_psm
        fields = [
            "id_user",
            "deskripsi_hasil",
            "tanggal",
            "jumlah_kegiatan",
            "satker_dibimtek",
            "rekomendasi",
            "satuan_kerja_pelaksana_kegiatan",
            "tindak_lanjut",
            "no",
            "simpulan",
            "hambatan_kendala",
            "file",
            "created",
            "last_updated",
        ]

class tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psm
        fields = [
            "id_tbl_pengumpulan_data_ikotan_pelaksanaan_psm",
            "nama_stakeholder",
            "kegiatan_yang_dilakukan",
            "nasional",
            "provinsi",
            "kota_kabupaten",
            "kecamatan",
            "kelurahan_desa",
            "linkungan",
            "jumlah_sasaran",
            "hasil_dampak",
            "kesimpulan",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_data_dukungan_stakeholder_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_data_dukungan_stakeholder_psm
        fields = [
            "id",
            "satuan_kerja",
            "created",
            "last_updated",
        ]

class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatif
        fields = [
            "id_user",
            "satuan_kerja",
            "created",
            "last_updated",
        ]

class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatif
        fields = [
            "id_tbl_monev_rangka_pendampingan_masyarakat_dayatif",
            "kesimpulan",
            "kegiatan_yang_dilakukan",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
            "jumlah_sasaran",
            "desa_kelurahan",
            "kota_kabupaten",
            "kecamatan",
            "nama_stakeholder",
            "hasil_dampak",
        ]

class tbl_kegiatan_bimtek_stakeholder_pendamping_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif
        fields = [
            "id_user",
            "satuan_kerja",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatif
        fields = [
            "no",
            "tanggal",
            "tindak_lanjut",
            "jumlah_peserta",
            "stakeholder_pendamping_yang_diundang",
            "deskripsi_hasil",
            "kendala_hambatan",
            "kesimpulan",
            "file",
            "created",
            "last_updated",
        ]

class tbl_kegiatan_lainnya_pelaksanaan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_kegiatan_lainnya_pelaksanaan_psm
        fields = [
            "id_tbl_kegiatan_lainnya_psm",
            "nama_kegiatan",
            "tempat",
            "waktu",
            "lingkungan_sasaran",
            "jumlah_orang",
            "hasil_dampak",
            "kesimpulan",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_kegiatan_lainnya_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_kegiatan_lainnya_psm
        fields = [
            "id_user",
            "satuan_kerja",
            "created",
            "last_updated",
        ]

class tbl_konsolidasi_kebijakan_pelaksanaan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_konsolidasi_kebijakan_pelaksanaan_psm
        fields = [
            "id_tbl_konsolidasi_kebijakan_psm",
            "no",
            "tanggal",
            "peserta",
            "stakeholde_pendamping_yang_diundang",
            "deskripsi_hasil",
            "hambatan_kendala",
            "kesimpulan",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_konsolidasi_kebijakan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_konsolidasi_kebijakan_psm
        fields = [
            "id_user",
            "satuan_kerja_pelaksana_kegiatan",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatif
        fields = [
            "id_user",
            "satuan_kerja",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatif
        fields = [
            "id_tbl_monev_pemberdayaan_detail",
            "nilai",
            "deskripsi_hasil",
            "ibm",
            "tanggal",
            "last_updated",
            "jenis_pelatihan",
            "simpulan",
            "kategori",
            "file",
            "nama_kawasan",
            "wanita",
            "created",
            "jumlah_peserta",
            "tindak_lanjut",
            "no",
            "daftar_nama_peserta",
            "desa_bersinar",
            "pria",
        ]

class tbl_monev_rangka_pendampingan_masyarakat_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_monev_rangka_pendampingan_masyarakat_dayatif
        fields = [
            "id_user",
            "satuan_kerja",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_monev_rangka_pendampingan_masyarakat_detail_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_monev_rangka_pendampingan_masyarakat_detail_dayatif
        fields = [
            "id_tbl_monev_rangka_pendampingan_masyarakat_dayatif",
            "simpulan",
            "created",
            "tindak_lanjut",
            "no",
            "deskripsi_hasil",
            "tanggal",
            "file",
            "lokasi",
            "last_updated",
        ]

class tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psm
        fields = [
            "id_tbl_monev_supervisi_kegiatan_kotan_psm",
            "no",
            "nama_lingkungan_dan_satker",
            "nama_jabatan",
            "jenis_kelamin",
            "jumlah_peserta",
            "status_indeks_kemandirian_partisipasi",
            "nilai_skp",
            "status",
            "deskripsi_hasil",
            "simpulan",
            "tidak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_monev_supervisi_kegiatan_kotan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_monev_supervisi_kegiatan_kotan_psm
        fields = [
            "id_user",
            "satuan_kerja",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatif
        fields = [
            "id_user",
            "satuan_kerja",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatif
        fields = [
            "id_tbl_pemetaan_potensi_detail",
            "kesimpulan",
            "kendala_hambatan",
            "last_updated",
            "file",
            "deskripsi_hasil",
            "lokasi",
            "tindak_lanjut",
            "created",
            "tanggal",
            "no",
        ]

class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatif
        fields = [
            "id_user",
            "jumlah_kegiatan",
            "satuan_kerja",
            "created",
            "last_updated",
        ]

class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatif
        fields = [
            "id_tbl_pemetaan_stakeholder_detail",
            "created",
            "deskripsi_hasil",
            "no",
            "lokasi",
            "tindak_lanjut",
            "tanggal",
            "kesimpulan",
            "last_updated",
            "file",
            "kendala_hambatan",
        ]

class tbl_pengumpulan_data_ikotan_pelaksanaan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_pengumpulan_data_ikotan_pelaksanaan_psm
        fields = [
            "id_tbl_pengumpulan_data_ikotan_pelaksanaan_psm",
            "no",
            "tanggal",
            "nama_responden",
            "deskripsi_hasil",
            "simpulan",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_pengumpulan_data_ikotan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_pengumpulan_data_ikotan_psm
        fields = [
            "created",
            "last_updated",
            "id_user",
            "unit_observasi",
            "jumlah_kegiatan",
        ]

class tbl_rakernis_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_rakernis_psm
        fields = [
            "id_user",
            "satuan_kerja_pelaksana_kegiatan",
            "satker_bnnp_bnnk_diundang",
            "deskripsi_hasil",
            "rekomendasi",
            "hambatan_kendala",
            "tanggal",
            "simpulan",
            "file",
            "created",
            "last_updated",
        ]

class tbl_rakor_pemetaan_pelaksanaan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_rakor_pemetaan_pelaksanaan_psm
        fields = [
            "id_tbl_rakor_pemetaan_psm",
            "no",
            "tanggal",
            "peserta",
            "sasaran_lingkungan",
            "deskripsi_hasil",
            "hambatan_kendala",
            "kesimpulan",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_rakor_pemetaan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_rakor_pemetaan_psm
        fields = [
            "id_user",
            "satuan_kerja_pelaksana_kegiatan",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatif
        fields = [
            "id_user",
            "satuan_kerja",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatif
        fields = [
            "id_tbl_rekapitulasi_kegiatan_detail",
            "no",
            "tanggal",
            "jumlah_peserta",
            "stakeholder_pendamping_yang_diundang",
            "deskripsi_hasil",
            "kendala_hambatan",
            "kesimpulan",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_rekapitulasi_pembinaan_teknis_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_rekapitulasi_pembinaan_teknis_dayatif
        fields = [
            "id_user",
            "satuan_kerja",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_rekapitulasi_pembinaan_teknis_detail_dayatifSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_rekapitulasi_pembinaan_teknis_detail_dayatif
        fields = [
            "id_tbl_rekapitulasi_pembinaan_teknis_dayatif",
            "no",
            "tanggal",
            "satker_yang_dibimtek",
            "hambatan_kendala",
            "deskripsi_hasil",
            "tindak_lanjut",
            "simpulan",
            "file",
            "created",
            "last_updated",
        ]

class tbl_sinkronisasi_kebijakan_pelaksanaan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_sinkronisasi_kebijakan_pelaksanaan_psm
        fields = [
            "id_tbl_sinkronisasi_kebijakan_psm",
            "no",
            "tanggal",
            "jumlah_peserta",
            "stakeholder_yang_diundang",
            "deskripsi_hasil",
            "kendala_hambatan",
            "kesimpulan",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_sinkronisasi_kebijakan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_sinkronisasi_kebijakan_psm
        fields = [
            "id_user",
            "satuan_kerja",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_tes_urine_deteksi_dini_pelaksanaan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_tes_urine_deteksi_dini_pelaksanaan_psm
        fields = [
            "no",
            "tanggal",
            "nama_lingkungan",
            "jenis_kelamin",
            "jumlah_peserta",
            "nama",
            "hasil_tes_urine",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_tes_urine_deteksi_dini_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_tes_urine_deteksi_dini_psm
        fields = [
            "id_user",
            "satuan_kerja",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_workshop_penggiat_pelaksanaan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_workshop_penggiat_pelaksanaan_psm
        fields = [
            "id_tbl_workshop_penggiat_psm",
            "no",
            "tanggal",
            "peserta",
            "stakeholde_pendamping_yang_diundang",
            "deskripsi_hasil",
            "hambatan_kendala",
            "kesimpulan",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_workshop_penggiat_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_workshop_penggiat_psm
        fields = [
            "id_user",
            "satuan_kerja_pelaksana_kegiatan",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]

class tbl_workshop_tematik_pelaksanaan_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_workshop_tematik_pelaksanaan_psm
        fields = [
            "id_tbl_workshop_tematik",
            "no",
            "tanggal",
            "jumlah_peserta",
            "stakeholder_yang_diundang",
            "deskripsi_hasil",
            "kendala_hambatan",
            "kesimpulan",
            "tindak_lanjut",
            "file",
            "created",
            "last_updated",
        ]

class tbl_workshop_tematik_psmSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tbl_workshop_tematik_psm
        fields = [
            "id_user",
            "satuan_kerja",
            "jumlah_kegiatan",
            "created",
            "last_updated",
        ]