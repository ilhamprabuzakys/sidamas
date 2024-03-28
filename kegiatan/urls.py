from django.urls import path, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()

# ==== PSM ====
psm = routers.DefaultRouter()
psm.register("rakernis", api.PSM_RAKERNIS_ViewSet)
psm.register("binaan_teknis", api.PSM_BINAAN_TEKNIS_ViewSet)
psm.register("asistensi", api.PSM_ASISTENSI_ViewSet)
psm.register("tes_urine", api.PSM_TES_URINE_DETEKSI_DINI_ViewSet)
psm.register("tes_urine_crud", api.PSM_TES_URNIE_CURD_ViewSet) #crud;

# ==== DAYATIF ====
dayatif = routers.DefaultRouter()
dayatif.register("binaan_teknis", api.DAYATIF_BINAAN_TEKNIS_ViewSet, basename='binaan_teknis')
dayatif.register("pemetaan_potensi/list", api.DAYATIF_PEMETAAN_POTENSI_LIST_ViewSet, basename='pemetaan_potensi_list')
dayatif.register("pemetaan_potensi", api.DAYATIF_PEMETAAN_POTENSI_ViewSet, basename='pemetaan_potensi')

router.registry.extend(psm.registry)
router.registry.extend(dayatif.registry)

urlpatterns = (
    path("api/v1/psm/", include(psm.urls), name='psm-list'),
    path("api/v1/dayatif/", include(dayatif.urls), name='dayatif-list'),
    
    # API Root
    path("api/v1/", api.api_root, name="Daftar Direktorat"),

    # VIEW HALAMAN PSM
    path("psm/rakernis/",views.psm_rakernisView.as_view(),name="psm_rakernis",),
    path("psm/rakernis2/",views.psm_rakernis2View.as_view(),name="psm_rakernis2",),
    path("psm/rakernis3/",views.psm_rakernis3View.as_view(),name="psm_rakernis2",),
    path("psm/bintek/",views.psm_bintekView.as_view(),name="psm_bintek",),
    path("psm/rakor_pemetaan/",views.psm_rakor_pemetaanView.as_view(),name="psm_rakor_pemetaan",),
    path("psm/rakor_pemetaan2/",views.psm_rakor_pemetaanView_2.as_view(),name="psm_rakor_pemetaan2",),
    path("psm/audiensi/",views.psm_audiensiView.as_view(),name="psm_audiensi",),
    path("psm/konsolidasi_kebijakan/",views.psm_konsolidasi_kebijakanView.as_view(),name="psm_konsolidasi_kebijakan",),
    path("psm/workshop_penggiat/",views.psm_workshop_penggiatView.as_view(),name="psm_workshop_penggiat",),
    path("psm/bintek_peggiat_p4gn/",views.psm_bintek_peggiat_p4gnView.as_view(),name="psm_bintek_peggian_p4gn",),
    path("psm/sinkronisasi_kebijakan/",views.psm_sinkronisasi_kebijakanView.as_view(),name="psm_sinkronisasi_kebijakan",),
    path("psm/workshop_tematik/",views.psm_workshop_tematikView.as_view(),name="psm_workshop_tematik",),
    path("psm/asistensi/",views.psm_asistensiView.as_view(),name="psm_asistensi",),
    path("psm/tes_urine/",views.psm_tes_urine_deteksi_diniView.as_view(),name="psm_tes_urine",),
    path("psm/monev_supervisi_kegiatan_kotan/",views.psm_monev_supervisi_kegiatan_kotanView.as_view(),name="psm_monev_supervisi_kegiatan_kotan",),
    path("psm/pengumpulan_data_ikotan/",views.psm_pengumpulan_data_ikotanView.as_view(),name="psm_pengumpulan_data_ikotan",),
    path("psm/dukungan_stakeholder/",views.psm_dukungan_stakeholderView.as_view(),name="psm_dukungan_stakeholder",),
    path("psm/kegiatan_lainnya/",views.psm_kegiatan_lainnyaView.as_view(),name="psm_kegiatan_lainnya",),

    # VIEW HALAMAN DAYATIF
    path("dayatif/binaan_teknis2/",views.DAYATIF_BINAAN_TEKNIS2_View.as_view(),name="dayatif_binaan_teknis2",),
    path("dayatif/binaan_teknis/",views.DAYATIF_BINAAN_TEKNIS_View.as_view(),name="dayatif_binaan_teknis",),
    
    path("dayatif/pemetaan_potensi/",views.DAYATIF_PEMETAAN_POTENSI_View.as_view(),name="dayatif_pemetaan_potensi",),
    path("dayatif/pemetaan_stakeholder/",views.dayatif_pemetaan_stakeholderView.as_view(),name="dayatif_pemetaan_stakeholder",),
    path("dayatif/rapat_sinergi_stakeholder/",views.dayatif_rapat_sinergi_stakeholderView.as_view(),name="dayatif_rapat_sinergi_stakeholder",),
    path("dayatif/bimtek_stakeholder/",views.dayatif_bimtek_stakeholderView.as_view(),name="dayatif_bimtek_stakeholder",),
    path("dayatif/bimtek_lifeskill/",views.dayatif_bimtek_lifeskillView.as_view(),name="dayatif_bimtek_lifeskill",),
    path("dayatif/monev_dayatif/",views.dayatif_monev_dayatifView.as_view(),name="dayatif_monev_dayatif",),
    path("dayatif/monev_kewirausahaan_dan_ikkr/",views.dayatif_monev_kewirausahaan_dan_ikkrView.as_view(),name="dayatif_monev_kewirausahaan_dan_ikkr",),
    path("dayatif/monev_pendampingan/",views.dayatif_monev_pendampinganView.as_view(),name="dayatif_monev_pendampingan",),
    path("dayatif/data_dukungan_stakeholder/",views.dayatif_data_dukungan_stakeholderView.as_view(),name="dayatif_data_dukungan_stakeholder",),
    path("dayatif/dukungan_stakeholder/",views.dayatif_dukungan_stakeholderView.as_view(),name="dayatif_dukungan_stakeholder",),
)