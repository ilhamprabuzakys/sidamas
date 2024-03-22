from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from . import models
from . import forms
from users.models import Satker

class GlobalPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.is_staff == False and request.user.profile.role is None or request.user.profile.satker is None or request.user.profile.is_verified == False:
            user = self.request.user
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini."
            print(message)
            return HttpResponseRedirect(reverse("dashboard:profile"))
        return super().dispatch(request, *args, **kwargs)
    
# START PSM
class PsmPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.profile.role != 'psm':
            user = self.request.user
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini. Halaman ini khusus untuk direktorat Dayatif"
            print(message)
            return HttpResponseForbidden(message)
        return super().dispatch(request, *args, **kwargs)
    
class PSMBaseView(LoginRequiredMixin, GlobalPermissionMixin, PsmPermissionMixin):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class psm_rakernisView(PSMBaseView, View):
    template_name = "psm/rakernis/rakernis.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})
    
class psm_bintekView(PSMBaseView, View):
    template_name = "psm/bintek/bintek.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})
    
class psm_rakor_pemetaanView(PSMBaseView, View):
    template_name = "psm/rakor_pemetaan/rakor_pemetaan.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})
    
class psm_rakor_pemetaanView_2(PSMBaseView, View):
    template_name = "psm/rakor_pemetaan2/index.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class psm_audiensiView(PSMBaseView, View):
    template_name = "psm/audiensi/audiensi.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})
    
class psm_konsolidasi_kebijakanView(PSMBaseView, View):
    template_name = "psm/konsolidasi_kebijakan/konsolidasi_kebijakan.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class psm_workshop_penggiatView(PSMBaseView, View):
    template_name = "psm/workshop_penggiat/workshop_penggiat.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class psm_bintek_peggiat_p4gnView(PSMBaseView, View):
    template_name = "psm/bintek_penggiat_p4gn/bintek_penggiat_p4gn.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})
    
    
class psm_sinkronisasi_kebijakanView(PSMBaseView, View):
    template_name = "psm/sinkronisasi_kebijakan/sinkronisasi_kebijakan.html"
    
    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})
    
class psm_workshop_tematikView(PSMBaseView, View):
    template_name = "psm/workshop_tematik/workshop_tematik.html"
    
    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})
    
class psm_asistensiView(PSMBaseView, View):
    template_name = "psm/asistensi/asistensi.html"
    
    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})
    
class psm_tes_urine_deteksi_diniView(PSMBaseView, View):
    template_name = "psm/tes_urine_deteksi_dini/tes_urine_deteksi_dini.html"
    
    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})

class psm_monev_supervisi_kegiatan_kotanView(PSMBaseView, View):
    template_name = "psm/monev_supervisi_kegiatan_kotan/monev_supervisi_kegiatan_kotan.html"
    
    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})
    
class psm_pengumpulan_data_ikotanView(PSMBaseView, View):
    template_name = "psm/pengumpulan_data_ikotan/pengumpulan_data_ikotan.html"
    
    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})
    
class psm_dukungan_stakeholderView(PSMBaseView, View):
    template_name = "psm/dukungan_stakeholder/dukungan_stakeholder.html"
    
    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})
    
class psm_kegiatan_lainnyaView(PSMBaseView, View):
    template_name = "psm/kegiatan_lainnya/kegiatan_lainnya.html"
    
    def get(self, request):
            satker = Satker.objects.all()
            return render(request, self.template_name, {'satker' : satker})
# -- END PSM
    
class DayatifPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.profile.role != 'dayatif':
            user = self.request.user
            # print(f'Adalah dayatif : ', request.user.profile.role == 'dayatif')
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini. Halaman ini khusus untuk direktorat Dayatif"
            print(message)
            return HttpResponseForbidden(message)
        return super().dispatch(request, *args, **kwargs)

class DayatifBaseView(LoginRequiredMixin, GlobalPermissionMixin, DayatifPermissionMixin):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['satker'] = Satker.objects.all()
        return context
    
class dayatif_bintekView(DayatifBaseView, TemplateView):
    template_name = "dayatif/bintek/bintek.html"

class dayatif_pemetaan_potensiView(DayatifBaseView, View):
    template_name = "dayatif/pemetaan_potensi/pemetaan_potensi.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class dayatif_pemetaan_stakeholderView(DayatifBaseView, View):
    template_name = "dayatif/pemetaan_stakeholder/pemetaan_stakeholder.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})
        
class dayatif_rapat_sinergi_stakeholderView(DayatifBaseView, View):
    template_name = "dayatif/rapat_sinergi_stakeholder/rapat_sinergi_stakeholder.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class dayatif_bimtek_stakeholderView(DayatifBaseView, View):
    template_name = "dayatif/bimtek_stakeholder/bimtek_stakeholder.html"
    
    daftar_jenis_bimbingan = [
        {
            'value': 'bimbingan_teknis_stakeholder',
            'label': 'Bimbingan Teknis Stakeholder',
        },
        {
            'value': 'bimbingan_teknis_pendamping',
            'label': 'Bimbingan Teknis Pendamping',
        }
    ]
    
    def get(self, request):
        satker = Satker.objects.all()
        context = {
            'daftar_jenis_bimbingan' : self.daftar_jenis_bimbingan,
            'satker' : satker
        }
        return render(request, self.template_name, context)

class dayatif_bimtek_lifeskillView(DayatifBaseView, View):
    template_name = "dayatif/bimtek_lifeskill/bimtek_lifeskill.html"
    
    daftar_kerajinan = [
        {
            'value': 'Menjahit',
            'label': 'Menjahit',
        },
        {
            'value': 'Kerajinan Tangan',
            'label': 'Kerajinan Tangan',
        },
        {
            'value': 'Pengolahan Makanan',
            'label': 'Pengolahan Makanan',
        },
        {
            'value': 'Pembuatan Sabun',
            'label': 'Pembuatan Sabun',
        },
        {
            'value': 'Barista Kopi',
            'label': 'Barista Kopi',
        },
        {
            'value': '',
            'label': 'Lainnya',
        },
    ]
    
    def get(self, request):
        satker = Satker.objects.all()
        context = {
            'daftar_kerajinan' : self.daftar_kerajinan,
            'satker' : satker
        }
        return render(request, self.template_name, context)
    
class dayatif_monev_dayatifView(DayatifBaseView, View):
    template_name = "dayatif/monev_dayatif/monev_dayatif.html"
    
    daftar_jenis_rekapitulasi = [
        {
            'value': 'Monitoring dan Evaluasi Kerja',
            'label': 'Monitoring dan Evaluasi Kerja',
        },
        {
            'value': 'Monitoring dan Evaluasi Kerja dalam rangka Pendampingan',
            'label': 'Monitoring dan Evaluasi Kerja dalam rangka Pendampingan',
        },
    ]
    
    daftar_periode = [
        {
            'value': 'Triwulan',
            'label': 'Triwulan',
        },
        {
            'value': 'Semester',
            'label': 'Semester',
        },
        {
            'value': 'Tahunan',
            'label': 'Tahunan',
        },
    ]
    
    daftar_kerajinan = [
        {
            'value': 'Menjahit',
            'label': 'Menjahit',
        },
        {
            'value': 'Kerajinan Tangan',
            'label': 'Kerajinan Tangan',
        },
        {
            'value': 'Pengolahan Makanan',
            'label': 'Pengolahan Makanan',
        },
        {
            'value': 'Pembuatan Sabun',
            'label': 'Pembuatan Sabun',
        },
        {
            'value': 'Barista Kopi',
            'label': 'Barista Kopi',
        },
        {
            'value': '',
            'label': 'Lainnya',
        },
    ]
    
    def get(self, request):
        satker = Satker.objects.all()
        context = {
            'daftar_kerajinan' : self.daftar_kerajinan,
            'daftar_jenis_rekapitulasi' : self.daftar_jenis_rekapitulasi,
            'daftar_periode' : self.daftar_periode,
            'satker' : satker
        }
        return render(request, self.template_name, context)

class dayatif_monev_kewirausahaan_dan_ikkrView(DayatifBaseView, View):
    template_name = "dayatif/monev_kewirausahaan_dan_ikkr.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class dayatif_monev_pendampinganView(DayatifBaseView, View):
    template_name = "dayatif/monev_pendampingan.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})
    
class dayatif_data_dukungan_stakeholderView(DayatifBaseView, View):
    template_name = "dayatif/data_dukungan_stakeholder.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

class dayatif_dukungan_stakeholderView(DayatifBaseView, View):
    template_name = "dayatif/dukungan_stakeholder/dukungan_stakeholder.html"
    """
        1. Penerbitan regulasi P4GN
        2. Dukungan SDM
        3. Sarana dan Prasarana
        4. Dukungan Anggaran
        5. Dukungan Kegiatan
        6. Dukungan Sarana Produksi
        7. Dukungan Permodalan
        8. Lainnya
    """
    
    daftar_jenis_dukungan = [
        {
            'value': 'Penerbitan regulasi P4GN',
            'label': 'Penerbitan regulasi P4GN',
        },
        {
            'value': 'Dukungan SDM',
            'label': 'Dukungan SDM',
        },
        {
            'value': 'Sarana dan Prasarana',
            'label': 'Sarana dan Prasarana',
        },
        {
            'value': 'Dukungan Anggaran',
            'label': 'Dukungan Anggaran',
        },
        {
            'value': 'Dukungan Kegiatan',
            'label': 'Dukungan Kegiatan',
        },
        {
            'value': 'Dukungan Sarana Produksi',
            'label': 'Dukungan Sarana Produksi',
        },
        {
            'value': 'Dukungan Permodalan',
            'label': 'Dukungan Permodalan',
        },
        {
            'value': 'Lainnya',
            'label': 'Lainnya',
        },
    ]
    
    def get(self, request):
        satker = Satker.objects.all()
        context = {
            'satker' : satker,
            'daftar_jenis_dukungan' : self.daftar_jenis_dukungan,
        }
        return render(request, self.template_name, context)
    

class DAYATIF_BINAAN_TEKNIS_View(DayatifBaseView, TemplateView):
    template_name = "dayatif/binaan_teknis/binaan_teknis.html"