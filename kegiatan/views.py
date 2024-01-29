from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View, generic
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
    
# --START Dayatif (9 Module) (Yang baru cuma 8)
class DayatifPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.profile.role != 'dayatif':
            user = self.request.user
            # print(f'Adalah dayatif : ', request.user.profile.role == 'dayatif')
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini. Halaman ini khusus untuk direktorat Dayatif"
            print(message)
            return HttpResponseForbidden(message)
        return super().dispatch(request, *args, **kwargs)

class DayatifBaseView(GlobalPermissionMixin, DayatifPermissionMixin, LoginRequiredMixin):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['satker'] = Satker.objects.all()
        return context
    
class dayatif_bintekView(DayatifBaseView, View):
    template_name = "dayatif/bintek/bintek.html"
    
    def get(self, request):
        satker = Satker.objects.all()
        return render(request, self.template_name, {'satker' : satker})

# Contoh layout jika pakai rowspan dan colspan (datatable not supported)
class dayatif_revisi_bintekView(DayatifBaseView, View):
    template_name = "dayatif/bintek/bintek2.html"

    def get(self, request):
        satker = Satker.objects.all()
        context = {
            'satker' : satker,
            'jumlah_item' : range(3)
        }
        return render(request, self.template_name, context)

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
    
# --END Dayatif

# --START PSM (15 Module)
class PsmPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.profile.role != 'psm':
            user = self.request.user
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini. Halaman ini khusus untuk direktorat Dayatif"
            print(message)
            return HttpResponseForbidden(message)
        return super().dispatch(request, *args, **kwargs)

class PSMBaseView(PsmPermissionMixin, LoginRequiredMixin):
    
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
# --END PSM


class tbl_asistensi_pelaksanaan_psmListView(generic.ListView):
    model = models.tbl_asistensi_pelaksanaan_psm
    form_class = forms.tbl_asistensi_pelaksanaan_psmForm


class tbl_asistensi_pelaksanaan_psmCreateView(generic.CreateView):
    model = models.tbl_asistensi_pelaksanaan_psm
    form_class = forms.tbl_asistensi_pelaksanaan_psmForm


class tbl_asistensi_pelaksanaan_psmDetailView(generic.DetailView):
    model = models.tbl_asistensi_pelaksanaan_psm
    form_class = forms.tbl_asistensi_pelaksanaan_psmForm


class tbl_asistensi_pelaksanaan_psmUpdateView(generic.UpdateView):
    model = models.tbl_asistensi_pelaksanaan_psm
    form_class = forms.tbl_asistensi_pelaksanaan_psmForm
    pk_url_kwarg = "pk"


class tbl_asistensi_pelaksanaan_psmDeleteView(generic.DeleteView):
    model = models.tbl_asistensi_pelaksanaan_psm
    success_url = reverse_lazy("pelaporan_tbl_asistensi_pelaksanaan_psm_list")


class tbl_asistensi_psmListView(generic.ListView):
    model = models.tbl_asistensi_psm
    form_class = forms.tbl_asistensi_psmForm


class tbl_asistensi_psmCreateView(generic.CreateView):
    model = models.tbl_asistensi_psm
    form_class = forms.tbl_asistensi_psmForm


class tbl_asistensi_psmDetailView(generic.DetailView):
    model = models.tbl_asistensi_psm
    form_class = forms.tbl_asistensi_psmForm


class tbl_asistensi_psmUpdateView(generic.UpdateView):
    model = models.tbl_asistensi_psm
    form_class = forms.tbl_asistensi_psmForm
    pk_url_kwarg = "pk"


class tbl_asistensi_psmDeleteView(generic.DeleteView):
    model = models.tbl_asistensi_psm
    success_url = reverse_lazy("pelaporan_tbl_asistensi_psm_list")


class tbl_audiensi_pelaksanaan_psmListView(generic.ListView):
    model = models.tbl_audiensi_pelaksanaan_psm
    form_class = forms.tbl_audiensi_pelaksanaan_psmForm


class tbl_audiensi_pelaksanaan_psmCreateView(generic.CreateView):
    model = models.tbl_audiensi_pelaksanaan_psm
    form_class = forms.tbl_audiensi_pelaksanaan_psmForm


class tbl_audiensi_pelaksanaan_psmDetailView(generic.DetailView):
    model = models.tbl_audiensi_pelaksanaan_psm
    form_class = forms.tbl_audiensi_pelaksanaan_psmForm


class tbl_audiensi_pelaksanaan_psmUpdateView(generic.UpdateView):
    model = models.tbl_audiensi_pelaksanaan_psm
    form_class = forms.tbl_audiensi_pelaksanaan_psmForm
    pk_url_kwarg = "pk"


class tbl_audiensi_pelaksanaan_psmDeleteView(generic.DeleteView):
    model = models.tbl_audiensi_pelaksanaan_psm
    success_url = reverse_lazy("pelaporan_tbl_audiensi_pelaksanaan_psm_list")


class tbl_audiensi_psmListView(generic.ListView):
    model = models.tbl_audiensi_psm
    form_class = forms.tbl_audiensi_psmForm


class tbl_audiensi_psmCreateView(generic.CreateView):
    model = models.tbl_audiensi_psm
    form_class = forms.tbl_audiensi_psmForm


class tbl_audiensi_psmDetailView(generic.DetailView):
    model = models.tbl_audiensi_psm
    form_class = forms.tbl_audiensi_psmForm


class tbl_audiensi_psmUpdateView(generic.UpdateView):
    model = models.tbl_audiensi_psm
    form_class = forms.tbl_audiensi_psmForm
    pk_url_kwarg = "pk"


class tbl_audiensi_psmDeleteView(generic.DeleteView):
    model = models.tbl_audiensi_psm
    success_url = reverse_lazy("pelaporan_tbl_audiensi_psm_list")


class tbl_bimbingan_teknis_life_skill_dayatifListView(generic.ListView):
    model = models.tbl_bimbingan_teknis_life_skill_dayatif
    form_class = forms.tbl_bimbingan_teknis_life_skill_dayatifForm


class tbl_bimbingan_teknis_life_skill_dayatifCreateView(generic.CreateView):
    model = models.tbl_bimbingan_teknis_life_skill_dayatif
    form_class = forms.tbl_bimbingan_teknis_life_skill_dayatifForm


class tbl_bimbingan_teknis_life_skill_dayatifDetailView(generic.DetailView):
    model = models.tbl_bimbingan_teknis_life_skill_dayatif
    form_class = forms.tbl_bimbingan_teknis_life_skill_dayatifForm


class tbl_bimbingan_teknis_life_skill_dayatifUpdateView(generic.UpdateView):
    model = models.tbl_bimbingan_teknis_life_skill_dayatif
    form_class = forms.tbl_bimbingan_teknis_life_skill_dayatifForm
    pk_url_kwarg = "pk"


class tbl_bimbingan_teknis_life_skill_dayatifDeleteView(generic.DeleteView):
    model = models.tbl_bimbingan_teknis_life_skill_dayatif
    success_url = reverse_lazy("pelaporan_tbl_bimbingan_teknis_life_skill_dayatif_list")


class tbl_bimbingan_teknis_life_skill_detail_dayatifListView(generic.ListView):
    model = models.tbl_bimbingan_teknis_life_skill_detail_dayatif
    form_class = forms.tbl_bimbingan_teknis_life_skill_detail_dayatifForm


class tbl_bimbingan_teknis_life_skill_detail_dayatifCreateView(generic.CreateView):
    model = models.tbl_bimbingan_teknis_life_skill_detail_dayatif
    form_class = forms.tbl_bimbingan_teknis_life_skill_detail_dayatifForm


class tbl_bimbingan_teknis_life_skill_detail_dayatifDetailView(generic.DetailView):
    model = models.tbl_bimbingan_teknis_life_skill_detail_dayatif
    form_class = forms.tbl_bimbingan_teknis_life_skill_detail_dayatifForm


class tbl_bimbingan_teknis_life_skill_detail_dayatifUpdateView(generic.UpdateView):
    model = models.tbl_bimbingan_teknis_life_skill_detail_dayatif
    form_class = forms.tbl_bimbingan_teknis_life_skill_detail_dayatifForm
    pk_url_kwarg = "pk"


class tbl_bimbingan_teknis_life_skill_detail_dayatifDeleteView(generic.DeleteView):
    model = models.tbl_bimbingan_teknis_life_skill_detail_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_bimbingan_teknis_life_skill_detail_dayatif_list"
    )


class tbl_bimtek_penggiat_p4gn_lingkungan_psmListView(generic.ListView):
    model = models.tbl_bimtek_penggiat_p4gn_lingkungan_psm
    form_class = forms.tbl_bimtek_penggiat_p4gn_lingkungan_psmForm


class tbl_bimtek_penggiat_p4gn_lingkungan_psmCreateView(generic.CreateView):
    model = models.tbl_bimtek_penggiat_p4gn_lingkungan_psm
    form_class = forms.tbl_bimtek_penggiat_p4gn_lingkungan_psmForm


class tbl_bimtek_penggiat_p4gn_lingkungan_psmDetailView(generic.DetailView):
    model = models.tbl_bimtek_penggiat_p4gn_lingkungan_psm
    form_class = forms.tbl_bimtek_penggiat_p4gn_lingkungan_psmForm


class tbl_bimtek_penggiat_p4gn_lingkungan_psmUpdateView(generic.UpdateView):
    model = models.tbl_bimtek_penggiat_p4gn_lingkungan_psm
    form_class = forms.tbl_bimtek_penggiat_p4gn_lingkungan_psmForm
    pk_url_kwarg = "pk"


class tbl_bimtek_penggiat_p4gn_lingkungan_psmDeleteView(generic.DeleteView):
    model = models.tbl_bimtek_penggiat_p4gn_lingkungan_psm
    success_url = reverse_lazy("pelaporan_tbl_bimtek_penggiat_p4gn_lingkungan_psm_list")


class tbl_bimtek_penggiat_p4gn_psmListView(generic.ListView):
    model = models.tbl_bimtek_penggiat_p4gn_psm
    form_class = forms.tbl_bimtek_penggiat_p4gn_psmForm


class tbl_bimtek_penggiat_p4gn_psmCreateView(generic.CreateView):
    model = models.tbl_bimtek_penggiat_p4gn_psm
    form_class = forms.tbl_bimtek_penggiat_p4gn_psmForm


class tbl_bimtek_penggiat_p4gn_psmDetailView(generic.DetailView):
    model = models.tbl_bimtek_penggiat_p4gn_psm
    form_class = forms.tbl_bimtek_penggiat_p4gn_psmForm


class tbl_bimtek_penggiat_p4gn_psmUpdateView(generic.UpdateView):
    model = models.tbl_bimtek_penggiat_p4gn_psm
    form_class = forms.tbl_bimtek_penggiat_p4gn_psmForm
    pk_url_kwarg = "pk"


class tbl_bimtek_penggiat_p4gn_psmDeleteView(generic.DeleteView):
    model = models.tbl_bimtek_penggiat_p4gn_psm
    success_url = reverse_lazy("pelaporan_tbl_bimtek_penggiat_p4gn_psm_list")


class tbl_bimtek_psmListView(generic.ListView):
    model = models.tbl_bimtek_psm
    form_class = forms.tbl_bimtek_psmForm


class tbl_bimtek_psmCreateView(generic.CreateView):
    model = models.tbl_bimtek_psm
    form_class = forms.tbl_bimtek_psmForm


class tbl_bimtek_psmDetailView(generic.DetailView):
    model = models.tbl_bimtek_psm
    form_class = forms.tbl_bimtek_psmForm


class tbl_bimtek_psmUpdateView(generic.UpdateView):
    model = models.tbl_bimtek_psm
    form_class = forms.tbl_bimtek_psmForm
    pk_url_kwarg = "pk"


class tbl_bimtek_psmDeleteView(generic.DeleteView):
    model = models.tbl_bimtek_psm
    success_url = reverse_lazy("pelaporan_tbl_bimtek_psm_list")


class tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psmListView(generic.ListView):
    model = models.tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psm
    form_class = forms.tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psmForm


class tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psmCreateView(
    generic.CreateView
):
    model = models.tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psm
    form_class = forms.tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psmForm


class tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psmDetailView(
    generic.DetailView
):
    model = models.tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psm
    form_class = forms.tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psmForm


class tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psmUpdateView(
    generic.UpdateView
):
    model = models.tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psm
    form_class = forms.tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psmForm
    pk_url_kwarg = "pk"


class tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psmDeleteView(
    generic.DeleteView
):
    model = models.tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psm
    success_url = reverse_lazy(
        "pelaporan_tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psm_list"
    )


class tbl_data_dukungan_stakeholder_psmListView(generic.ListView):
    model = models.tbl_data_dukungan_stakeholder_psm
    form_class = forms.tbl_data_dukungan_stakeholder_psmForm


class tbl_data_dukungan_stakeholder_psmCreateView(generic.CreateView):
    model = models.tbl_data_dukungan_stakeholder_psm
    form_class = forms.tbl_data_dukungan_stakeholder_psmForm


class tbl_data_dukungan_stakeholder_psmDetailView(generic.DetailView):
    model = models.tbl_data_dukungan_stakeholder_psm
    form_class = forms.tbl_data_dukungan_stakeholder_psmForm


class tbl_data_dukungan_stakeholder_psmUpdateView(generic.UpdateView):
    model = models.tbl_data_dukungan_stakeholder_psm
    form_class = forms.tbl_data_dukungan_stakeholder_psmForm
    pk_url_kwarg = "pk"


class tbl_data_dukungan_stakeholder_psmDeleteView(generic.DeleteView):
    model = models.tbl_data_dukungan_stakeholder_psm
    success_url = reverse_lazy("pelaporan_tbl_data_dukungan_stakeholder_psm_list")


class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatifListView(
    generic.ListView
):
    model = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatif
    form_class = (
        forms.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatifForm
    )


class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatifCreateView(
    generic.CreateView
):
    model = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatif
    form_class = (
        forms.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatifForm
    )


class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatifDetailView(
    generic.DetailView
):
    model = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatif
    form_class = (
        forms.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatifForm
    )


class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatifUpdateView(
    generic.UpdateView
):
    model = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatif
    form_class = (
        forms.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatifForm
    )
    pk_url_kwarg = "pk"


class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatifDeleteView(
    generic.DeleteView
):
    model = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatif_list"
    )


class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatifListView(
    generic.ListView
):
    model = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatif
    form_class = (
        forms.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatifForm
    )


class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatifCreateView(
    generic.CreateView
):
    model = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatif
    form_class = (
        forms.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatifForm
    )


class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatifDetailView(
    generic.DetailView
):
    model = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatif
    form_class = (
        forms.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatifForm
    )


class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatifUpdateView(
    generic.UpdateView
):
    model = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatif
    form_class = (
        forms.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatifForm
    )
    pk_url_kwarg = "pk"


class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatifDeleteView(
    generic.DeleteView
):
    model = models.tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatif_list"
    )


class tbl_kegiatan_bimtek_stakeholder_pendamping_dayatifListView(generic.ListView):
    model = models.tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif
    form_class = forms.tbl_kegiatan_bimtek_stakeholder_pendamping_dayatifForm


class tbl_kegiatan_bimtek_stakeholder_pendamping_dayatifCreateView(generic.CreateView):
    model = models.tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif
    form_class = forms.tbl_kegiatan_bimtek_stakeholder_pendamping_dayatifForm


class tbl_kegiatan_bimtek_stakeholder_pendamping_dayatifDetailView(generic.DetailView):
    model = models.tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif
    form_class = forms.tbl_kegiatan_bimtek_stakeholder_pendamping_dayatifForm


class tbl_kegiatan_bimtek_stakeholder_pendamping_dayatifUpdateView(generic.UpdateView):
    model = models.tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif
    form_class = forms.tbl_kegiatan_bimtek_stakeholder_pendamping_dayatifForm
    pk_url_kwarg = "pk"


class tbl_kegiatan_bimtek_stakeholder_pendamping_dayatifDeleteView(generic.DeleteView):
    model = models.tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif_list"
    )


class tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatifListView(
    generic.ListView
):
    model = models.tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatif
    form_class = forms.tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatifForm


class tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatifCreateView(
    generic.CreateView
):
    model = models.tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatif
    form_class = forms.tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatifForm


class tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatifDetailView(
    generic.DetailView
):
    model = models.tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatif
    form_class = forms.tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatifForm


class tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatifUpdateView(
    generic.UpdateView
):
    model = models.tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatif
    form_class = forms.tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatifForm
    pk_url_kwarg = "pk"


class tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatifDeleteView(
    generic.DeleteView
):
    model = models.tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatif_list"
    )


class tbl_kegiatan_lainnya_pelaksanaan_psmListView(generic.ListView):
    model = models.tbl_kegiatan_lainnya_pelaksanaan_psm
    form_class = forms.tbl_kegiatan_lainnya_pelaksanaan_psmForm


class tbl_kegiatan_lainnya_pelaksanaan_psmCreateView(generic.CreateView):
    model = models.tbl_kegiatan_lainnya_pelaksanaan_psm
    form_class = forms.tbl_kegiatan_lainnya_pelaksanaan_psmForm


class tbl_kegiatan_lainnya_pelaksanaan_psmDetailView(generic.DetailView):
    model = models.tbl_kegiatan_lainnya_pelaksanaan_psm
    form_class = forms.tbl_kegiatan_lainnya_pelaksanaan_psmForm


class tbl_kegiatan_lainnya_pelaksanaan_psmUpdateView(generic.UpdateView):
    model = models.tbl_kegiatan_lainnya_pelaksanaan_psm
    form_class = forms.tbl_kegiatan_lainnya_pelaksanaan_psmForm
    pk_url_kwarg = "pk"


class tbl_kegiatan_lainnya_pelaksanaan_psmDeleteView(generic.DeleteView):
    model = models.tbl_kegiatan_lainnya_pelaksanaan_psm
    success_url = reverse_lazy("pelaporan_tbl_kegiatan_lainnya_pelaksanaan_psm_list")


class tbl_kegiatan_lainnya_psmListView(generic.ListView):
    model = models.tbl_kegiatan_lainnya_psm
    form_class = forms.tbl_kegiatan_lainnya_psmForm


class tbl_kegiatan_lainnya_psmCreateView(generic.CreateView):
    model = models.tbl_kegiatan_lainnya_psm
    form_class = forms.tbl_kegiatan_lainnya_psmForm


class tbl_kegiatan_lainnya_psmDetailView(generic.DetailView):
    model = models.tbl_kegiatan_lainnya_psm
    form_class = forms.tbl_kegiatan_lainnya_psmForm


class tbl_kegiatan_lainnya_psmUpdateView(generic.UpdateView):
    model = models.tbl_kegiatan_lainnya_psm
    form_class = forms.tbl_kegiatan_lainnya_psmForm
    pk_url_kwarg = "pk"


class tbl_kegiatan_lainnya_psmDeleteView(generic.DeleteView):
    model = models.tbl_kegiatan_lainnya_psm
    success_url = reverse_lazy("pelaporan_tbl_kegiatan_lainnya_psm_list")


class tbl_konsolidasi_kebijakan_pelaksanaan_psmListView(generic.ListView):
    model = models.tbl_konsolidasi_kebijakan_pelaksanaan_psm
    form_class = forms.tbl_konsolidasi_kebijakan_pelaksanaan_psmForm


class tbl_konsolidasi_kebijakan_pelaksanaan_psmCreateView(generic.CreateView):
    model = models.tbl_konsolidasi_kebijakan_pelaksanaan_psm
    form_class = forms.tbl_konsolidasi_kebijakan_pelaksanaan_psmForm


class tbl_konsolidasi_kebijakan_pelaksanaan_psmDetailView(generic.DetailView):
    model = models.tbl_konsolidasi_kebijakan_pelaksanaan_psm
    form_class = forms.tbl_konsolidasi_kebijakan_pelaksanaan_psmForm


class tbl_konsolidasi_kebijakan_pelaksanaan_psmUpdateView(generic.UpdateView):
    model = models.tbl_konsolidasi_kebijakan_pelaksanaan_psm
    form_class = forms.tbl_konsolidasi_kebijakan_pelaksanaan_psmForm
    pk_url_kwarg = "pk"


class tbl_konsolidasi_kebijakan_pelaksanaan_psmDeleteView(generic.DeleteView):
    model = models.tbl_konsolidasi_kebijakan_pelaksanaan_psm
    success_url = reverse_lazy(
        "pelaporan_tbl_konsolidasi_kebijakan_pelaksanaan_psm_list"
    )


class tbl_konsolidasi_kebijakan_psmListView(generic.ListView):
    model = models.tbl_konsolidasi_kebijakan_psm
    form_class = forms.tbl_konsolidasi_kebijakan_psmForm


class tbl_konsolidasi_kebijakan_psmCreateView(generic.CreateView):
    model = models.tbl_konsolidasi_kebijakan_psm
    form_class = forms.tbl_konsolidasi_kebijakan_psmForm


class tbl_konsolidasi_kebijakan_psmDetailView(generic.DetailView):
    model = models.tbl_konsolidasi_kebijakan_psm
    form_class = forms.tbl_konsolidasi_kebijakan_psmForm


class tbl_konsolidasi_kebijakan_psmUpdateView(generic.UpdateView):
    model = models.tbl_konsolidasi_kebijakan_psm
    form_class = forms.tbl_konsolidasi_kebijakan_psmForm
    pk_url_kwarg = "pk"


class tbl_konsolidasi_kebijakan_psmDeleteView(generic.DeleteView):
    model = models.tbl_konsolidasi_kebijakan_psm
    success_url = reverse_lazy("pelaporan_tbl_konsolidasi_kebijakan_psm_list")


class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatifListView(
    generic.ListView
):
    model = models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatif
    form_class = (
        forms.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatifForm
    )


class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatifCreateView(
    generic.CreateView
):
    model = models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatif
    form_class = (
        forms.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatifForm
    )


class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatifDetailView(
    generic.DetailView
):
    model = models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatif
    form_class = (
        forms.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatifForm
    )


class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatifUpdateView(
    generic.UpdateView
):
    model = models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatif
    form_class = (
        forms.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatifForm
    )
    pk_url_kwarg = "pk"


class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatifDeleteView(
    generic.DeleteView
):
    model = models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatif_list"
    )


class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatifListView(
    generic.ListView
):
    model = (
        models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatif
    )
    form_class = (
        forms.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatifForm
    )


class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatifCreateView(
    generic.CreateView
):
    model = (
        models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatif
    )
    form_class = (
        forms.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatifForm
    )


class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatifDetailView(
    generic.DetailView
):
    model = (
        models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatif
    )
    form_class = (
        forms.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatifForm
    )


class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatifUpdateView(
    generic.UpdateView
):
    model = (
        models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatif
    )
    form_class = (
        forms.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatifForm
    )
    pk_url_kwarg = "pk"


class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatifDeleteView(
    generic.DeleteView
):
    model = (
        models.tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatif
    )
    success_url = reverse_lazy(
        "pelaporan_tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatif_list"
    )


class tbl_monev_rangka_pendampingan_masyarakat_dayatifListView(generic.ListView):
    model = models.tbl_monev_rangka_pendampingan_masyarakat_dayatif
    form_class = forms.tbl_monev_rangka_pendampingan_masyarakat_dayatifForm


class tbl_monev_rangka_pendampingan_masyarakat_dayatifCreateView(generic.CreateView):
    model = models.tbl_monev_rangka_pendampingan_masyarakat_dayatif
    form_class = forms.tbl_monev_rangka_pendampingan_masyarakat_dayatifForm


class tbl_monev_rangka_pendampingan_masyarakat_dayatifDetailView(generic.DetailView):
    model = models.tbl_monev_rangka_pendampingan_masyarakat_dayatif
    form_class = forms.tbl_monev_rangka_pendampingan_masyarakat_dayatifForm


class tbl_monev_rangka_pendampingan_masyarakat_dayatifUpdateView(generic.UpdateView):
    model = models.tbl_monev_rangka_pendampingan_masyarakat_dayatif
    form_class = forms.tbl_monev_rangka_pendampingan_masyarakat_dayatifForm
    pk_url_kwarg = "pk"


class tbl_monev_rangka_pendampingan_masyarakat_dayatifDeleteView(generic.DeleteView):
    model = models.tbl_monev_rangka_pendampingan_masyarakat_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_monev_rangka_pendampingan_masyarakat_dayatif_list"
    )


class tbl_monev_rangka_pendampingan_masyarakat_detail_dayatifListView(generic.ListView):
    model = models.tbl_monev_rangka_pendampingan_masyarakat_detail_dayatif
    form_class = forms.tbl_monev_rangka_pendampingan_masyarakat_detail_dayatifForm


class tbl_monev_rangka_pendampingan_masyarakat_detail_dayatifCreateView(
    generic.CreateView
):
    model = models.tbl_monev_rangka_pendampingan_masyarakat_detail_dayatif
    form_class = forms.tbl_monev_rangka_pendampingan_masyarakat_detail_dayatifForm


class tbl_monev_rangka_pendampingan_masyarakat_detail_dayatifDetailView(
    generic.DetailView
):
    model = models.tbl_monev_rangka_pendampingan_masyarakat_detail_dayatif
    form_class = forms.tbl_monev_rangka_pendampingan_masyarakat_detail_dayatifForm


class tbl_monev_rangka_pendampingan_masyarakat_detail_dayatifUpdateView(
    generic.UpdateView
):
    model = models.tbl_monev_rangka_pendampingan_masyarakat_detail_dayatif
    form_class = forms.tbl_monev_rangka_pendampingan_masyarakat_detail_dayatifForm
    pk_url_kwarg = "pk"


class tbl_monev_rangka_pendampingan_masyarakat_detail_dayatifDeleteView(
    generic.DeleteView
):
    model = models.tbl_monev_rangka_pendampingan_masyarakat_detail_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_monev_rangka_pendampingan_masyarakat_detail_dayatif_list"
    )


class tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psmListView(generic.ListView):
    model = models.tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psm
    form_class = forms.tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psmForm


class tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psmCreateView(generic.CreateView):
    model = models.tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psm
    form_class = forms.tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psmForm


class tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psmDetailView(generic.DetailView):
    model = models.tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psm
    form_class = forms.tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psmForm


class tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psmUpdateView(generic.UpdateView):
    model = models.tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psm
    form_class = forms.tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psmForm
    pk_url_kwarg = "pk"


class tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psmDeleteView(generic.DeleteView):
    model = models.tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psm
    success_url = reverse_lazy(
        "pelaporan_tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psm_list"
    )


class tbl_monev_supervisi_kegiatan_kotan_psmListView(generic.ListView):
    model = models.tbl_monev_supervisi_kegiatan_kotan_psm
    form_class = forms.tbl_monev_supervisi_kegiatan_kotan_psmForm


class tbl_monev_supervisi_kegiatan_kotan_psmCreateView(generic.CreateView):
    model = models.tbl_monev_supervisi_kegiatan_kotan_psm
    form_class = forms.tbl_monev_supervisi_kegiatan_kotan_psmForm


class tbl_monev_supervisi_kegiatan_kotan_psmDetailView(generic.DetailView):
    model = models.tbl_monev_supervisi_kegiatan_kotan_psm
    form_class = forms.tbl_monev_supervisi_kegiatan_kotan_psmForm


class tbl_monev_supervisi_kegiatan_kotan_psmUpdateView(generic.UpdateView):
    model = models.tbl_monev_supervisi_kegiatan_kotan_psm
    form_class = forms.tbl_monev_supervisi_kegiatan_kotan_psmForm
    pk_url_kwarg = "pk"


class tbl_monev_supervisi_kegiatan_kotan_psmDeleteView(generic.DeleteView):
    model = models.tbl_monev_supervisi_kegiatan_kotan_psm
    success_url = reverse_lazy("pelaporan_tbl_monev_supervisi_kegiatan_kotan_psm_list")


class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatifListView(
    generic.ListView
):
    model = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatif
    form_class = (
        forms.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatifForm
    )


class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatifCreateView(
    generic.CreateView
):
    model = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatif
    form_class = (
        forms.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatifForm
    )


class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatifDetailView(
    generic.DetailView
):
    model = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatif
    form_class = (
        forms.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatifForm
    )


class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatifUpdateView(
    generic.UpdateView
):
    model = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatif
    form_class = (
        forms.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatifForm
    )
    pk_url_kwarg = "pk"


class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatifDeleteView(
    generic.DeleteView
):
    model = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatif_list"
    )


class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatifListView(
    generic.ListView
):
    model = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatif
    form_class = (
        forms.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatifForm
    )


class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatifCreateView(
    generic.CreateView
):
    model = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatif
    form_class = (
        forms.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatifForm
    )


class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatifDetailView(
    generic.DetailView
):
    model = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatif
    form_class = (
        forms.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatifForm
    )


class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatifUpdateView(
    generic.UpdateView
):
    model = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatif
    form_class = (
        forms.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatifForm
    )
    pk_url_kwarg = "pk"


class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatifDeleteView(
    generic.DeleteView
):
    model = models.tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatif_list"
    )


class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatifListView(
    generic.ListView
):
    model = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatif
    form_class = forms.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatifForm


class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatifCreateView(
    generic.CreateView
):
    model = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatif
    form_class = forms.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatifForm


class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatifDetailView(
    generic.DetailView
):
    model = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatif
    form_class = forms.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatifForm


class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatifUpdateView(
    generic.UpdateView
):
    model = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatif
    form_class = forms.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatifForm
    pk_url_kwarg = "pk"


class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatifDeleteView(
    generic.DeleteView
):
    model = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatif_list"
    )


class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatifListView(
    generic.ListView
):
    model = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatif
    form_class = (
        forms.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatifForm
    )


class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatifCreateView(
    generic.CreateView
):
    model = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatif
    form_class = (
        forms.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatifForm
    )


class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatifDetailView(
    generic.DetailView
):
    model = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatif
    form_class = (
        forms.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatifForm
    )


class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatifUpdateView(
    generic.UpdateView
):
    model = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatif
    form_class = (
        forms.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatifForm
    )
    pk_url_kwarg = "pk"


class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatifDeleteView(
    generic.DeleteView
):
    model = models.tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatif_list"
    )


class tbl_pengumpulan_data_ikotan_pelaksanaan_psmListView(generic.ListView):
    model = models.tbl_pengumpulan_data_ikotan_pelaksanaan_psm
    form_class = forms.tbl_pengumpulan_data_ikotan_pelaksanaan_psmForm


class tbl_pengumpulan_data_ikotan_pelaksanaan_psmCreateView(generic.CreateView):
    model = models.tbl_pengumpulan_data_ikotan_pelaksanaan_psm
    form_class = forms.tbl_pengumpulan_data_ikotan_pelaksanaan_psmForm


class tbl_pengumpulan_data_ikotan_pelaksanaan_psmDetailView(generic.DetailView):
    model = models.tbl_pengumpulan_data_ikotan_pelaksanaan_psm
    form_class = forms.tbl_pengumpulan_data_ikotan_pelaksanaan_psmForm


class tbl_pengumpulan_data_ikotan_pelaksanaan_psmUpdateView(generic.UpdateView):
    model = models.tbl_pengumpulan_data_ikotan_pelaksanaan_psm
    form_class = forms.tbl_pengumpulan_data_ikotan_pelaksanaan_psmForm
    pk_url_kwarg = "pk"


class tbl_pengumpulan_data_ikotan_pelaksanaan_psmDeleteView(generic.DeleteView):
    model = models.tbl_pengumpulan_data_ikotan_pelaksanaan_psm
    success_url = reverse_lazy(
        "pelaporan_tbl_pengumpulan_data_ikotan_pelaksanaan_psm_list"
    )


class tbl_pengumpulan_data_ikotan_psmListView(generic.ListView):
    model = models.tbl_pengumpulan_data_ikotan_psm
    form_class = forms.tbl_pengumpulan_data_ikotan_psmForm


class tbl_pengumpulan_data_ikotan_psmCreateView(generic.CreateView):
    model = models.tbl_pengumpulan_data_ikotan_psm
    form_class = forms.tbl_pengumpulan_data_ikotan_psmForm


class tbl_pengumpulan_data_ikotan_psmDetailView(generic.DetailView):
    model = models.tbl_pengumpulan_data_ikotan_psm
    form_class = forms.tbl_pengumpulan_data_ikotan_psmForm


class tbl_pengumpulan_data_ikotan_psmUpdateView(generic.UpdateView):
    model = models.tbl_pengumpulan_data_ikotan_psm
    form_class = forms.tbl_pengumpulan_data_ikotan_psmForm
    pk_url_kwarg = "pk"


class tbl_pengumpulan_data_ikotan_psmDeleteView(generic.DeleteView):
    model = models.tbl_pengumpulan_data_ikotan_psm
    success_url = reverse_lazy("pelaporan_tbl_pengumpulan_data_ikotan_psm_list")


class tbl_rakernis_psmListView(generic.ListView):
    model = models.tbl_rakernis_psm
    form_class = forms.tbl_rakernis_psmForm


class tbl_rakernis_psmCreateView(generic.CreateView):
    model = models.tbl_rakernis_psm
    form_class = forms.tbl_rakernis_psmForm


class tbl_rakernis_psmDetailView(generic.DetailView):
    model = models.tbl_rakernis_psm
    form_class = forms.tbl_rakernis_psmForm


class tbl_rakernis_psmUpdateView(generic.UpdateView):
    model = models.tbl_rakernis_psm
    form_class = forms.tbl_rakernis_psmForm
    pk_url_kwarg = "pk"


class tbl_rakernis_psmDeleteView(generic.DeleteView):
    model = models.tbl_rakernis_psm
    success_url = reverse_lazy("pelaporan_tbl_rakernis_psm_list")


class tbl_rakor_pemetaan_pelaksanaan_psmListView(generic.ListView):
    model = models.tbl_rakor_pemetaan_pelaksanaan_psm
    form_class = forms.tbl_rakor_pemetaan_pelaksanaan_psmForm


class tbl_rakor_pemetaan_pelaksanaan_psmCreateView(generic.CreateView):
    model = models.tbl_rakor_pemetaan_pelaksanaan_psm
    form_class = forms.tbl_rakor_pemetaan_pelaksanaan_psmForm


class tbl_rakor_pemetaan_pelaksanaan_psmDetailView(generic.DetailView):
    model = models.tbl_rakor_pemetaan_pelaksanaan_psm
    form_class = forms.tbl_rakor_pemetaan_pelaksanaan_psmForm


class tbl_rakor_pemetaan_pelaksanaan_psmUpdateView(generic.UpdateView):
    model = models.tbl_rakor_pemetaan_pelaksanaan_psm
    form_class = forms.tbl_rakor_pemetaan_pelaksanaan_psmForm
    pk_url_kwarg = "pk"


class tbl_rakor_pemetaan_pelaksanaan_psmDeleteView(generic.DeleteView):
    model = models.tbl_rakor_pemetaan_pelaksanaan_psm
    success_url = reverse_lazy("pelaporan_tbl_rakor_pemetaan_pelaksanaan_psm_list")


class tbl_rakor_pemetaan_psmListView(generic.ListView):
    model = models.tbl_rakor_pemetaan_psm
    form_class = forms.tbl_rakor_pemetaan_psmForm


class tbl_rakor_pemetaan_psmCreateView(generic.CreateView):
    model = models.tbl_rakor_pemetaan_psm
    form_class = forms.tbl_rakor_pemetaan_psmForm


class tbl_rakor_pemetaan_psmDetailView(generic.DetailView):
    model = models.tbl_rakor_pemetaan_psm
    form_class = forms.tbl_rakor_pemetaan_psmForm


class tbl_rakor_pemetaan_psmUpdateView(generic.UpdateView):
    model = models.tbl_rakor_pemetaan_psm
    form_class = forms.tbl_rakor_pemetaan_psmForm
    pk_url_kwarg = "pk"


class tbl_rakor_pemetaan_psmDeleteView(generic.DeleteView):
    model = models.tbl_rakor_pemetaan_psm
    success_url = reverse_lazy("pelaporan_tbl_rakor_pemetaan_psm_list")


class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatifListView(
    generic.ListView
):
    model = models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatif
    form_class = (
        forms.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatifForm
    )


class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatifCreateView(
    generic.CreateView
):
    model = models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatif
    form_class = (
        forms.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatifForm
    )


class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatifDetailView(
    generic.DetailView
):
    model = models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatif
    form_class = (
        forms.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatifForm
    )


class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatifUpdateView(
    generic.UpdateView
):
    model = models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatif
    form_class = (
        forms.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatifForm
    )
    pk_url_kwarg = "pk"


class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatifDeleteView(
    generic.DeleteView
):
    model = models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatif_list"
    )


class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatifListView(
    generic.ListView
):
    model = (
        models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatif
    )
    form_class = (
        forms.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatifForm
    )


class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatifCreateView(
    generic.CreateView
):
    model = (
        models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatif
    )
    form_class = (
        forms.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatifForm
    )


class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatifDetailView(
    generic.DetailView
):
    model = (
        models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatif
    )
    form_class = (
        forms.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatifForm
    )


class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatifUpdateView(
    generic.UpdateView
):
    model = (
        models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatif
    )
    form_class = (
        forms.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatifForm
    )
    pk_url_kwarg = "pk"


class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatifDeleteView(
    generic.DeleteView
):
    model = (
        models.tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatif
    )
    success_url = reverse_lazy(
        "pelaporan_tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatif_list"
    )


class tbl_rekapitulasi_pembinaan_teknis_dayatifListView(generic.ListView):
    model = models.tbl_rekapitulasi_pembinaan_teknis_dayatif
    form_class = forms.tbl_rekapitulasi_pembinaan_teknis_dayatifForm


class tbl_rekapitulasi_pembinaan_teknis_dayatifCreateView(generic.CreateView):
    model = models.tbl_rekapitulasi_pembinaan_teknis_dayatif
    form_class = forms.tbl_rekapitulasi_pembinaan_teknis_dayatifForm


class tbl_rekapitulasi_pembinaan_teknis_dayatifDetailView(generic.DetailView):
    model = models.tbl_rekapitulasi_pembinaan_teknis_dayatif
    form_class = forms.tbl_rekapitulasi_pembinaan_teknis_dayatifForm


class tbl_rekapitulasi_pembinaan_teknis_dayatifUpdateView(generic.UpdateView):
    model = models.tbl_rekapitulasi_pembinaan_teknis_dayatif
    form_class = forms.tbl_rekapitulasi_pembinaan_teknis_dayatifForm
    pk_url_kwarg = "pk"


class tbl_rekapitulasi_pembinaan_teknis_dayatifDeleteView(generic.DeleteView):
    model = models.tbl_rekapitulasi_pembinaan_teknis_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_rekapitulasi_pembinaan_teknis_dayatif_list"
    )


class tbl_rekapitulasi_pembinaan_teknis_detail_dayatifListView(generic.ListView):
    model = models.tbl_rekapitulasi_pembinaan_teknis_detail_dayatif
    form_class = forms.tbl_rekapitulasi_pembinaan_teknis_detail_dayatifForm


class tbl_rekapitulasi_pembinaan_teknis_detail_dayatifCreateView(generic.CreateView):
    model = models.tbl_rekapitulasi_pembinaan_teknis_detail_dayatif
    form_class = forms.tbl_rekapitulasi_pembinaan_teknis_detail_dayatifForm


class tbl_rekapitulasi_pembinaan_teknis_detail_dayatifDetailView(generic.DetailView):
    model = models.tbl_rekapitulasi_pembinaan_teknis_detail_dayatif
    form_class = forms.tbl_rekapitulasi_pembinaan_teknis_detail_dayatifForm


class tbl_rekapitulasi_pembinaan_teknis_detail_dayatifUpdateView(generic.UpdateView):
    model = models.tbl_rekapitulasi_pembinaan_teknis_detail_dayatif
    form_class = forms.tbl_rekapitulasi_pembinaan_teknis_detail_dayatifForm
    pk_url_kwarg = "pk"


class tbl_rekapitulasi_pembinaan_teknis_detail_dayatifDeleteView(generic.DeleteView):
    model = models.tbl_rekapitulasi_pembinaan_teknis_detail_dayatif
    success_url = reverse_lazy(
        "pelaporan_tbl_rekapitulasi_pembinaan_teknis_detail_dayatif_list"
    )


class tbl_sinkronisasi_kebijakan_pelaksanaan_psmListView(generic.ListView):
    model = models.tbl_sinkronisasi_kebijakan_pelaksanaan_psm
    form_class = forms.tbl_sinkronisasi_kebijakan_pelaksanaan_psmForm


class tbl_sinkronisasi_kebijakan_pelaksanaan_psmCreateView(generic.CreateView):
    model = models.tbl_sinkronisasi_kebijakan_pelaksanaan_psm
    form_class = forms.tbl_sinkronisasi_kebijakan_pelaksanaan_psmForm


class tbl_sinkronisasi_kebijakan_pelaksanaan_psmDetailView(generic.DetailView):
    model = models.tbl_sinkronisasi_kebijakan_pelaksanaan_psm
    form_class = forms.tbl_sinkronisasi_kebijakan_pelaksanaan_psmForm


class tbl_sinkronisasi_kebijakan_pelaksanaan_psmUpdateView(generic.UpdateView):
    model = models.tbl_sinkronisasi_kebijakan_pelaksanaan_psm
    form_class = forms.tbl_sinkronisasi_kebijakan_pelaksanaan_psmForm
    pk_url_kwarg = "pk"


class tbl_sinkronisasi_kebijakan_pelaksanaan_psmDeleteView(generic.DeleteView):
    model = models.tbl_sinkronisasi_kebijakan_pelaksanaan_psm
    success_url = reverse_lazy(
        "pelaporan_tbl_sinkronisasi_kebijakan_pelaksanaan_psm_list"
    )


class tbl_sinkronisasi_kebijakan_psmListView(generic.ListView):
    model = models.tbl_sinkronisasi_kebijakan_psm
    form_class = forms.tbl_sinkronisasi_kebijakan_psmForm


class tbl_sinkronisasi_kebijakan_psmCreateView(generic.CreateView):
    model = models.tbl_sinkronisasi_kebijakan_psm
    form_class = forms.tbl_sinkronisasi_kebijakan_psmForm


class tbl_sinkronisasi_kebijakan_psmDetailView(generic.DetailView):
    model = models.tbl_sinkronisasi_kebijakan_psm
    form_class = forms.tbl_sinkronisasi_kebijakan_psmForm


class tbl_sinkronisasi_kebijakan_psmUpdateView(generic.UpdateView):
    model = models.tbl_sinkronisasi_kebijakan_psm
    form_class = forms.tbl_sinkronisasi_kebijakan_psmForm
    pk_url_kwarg = "pk"


class tbl_sinkronisasi_kebijakan_psmDeleteView(generic.DeleteView):
    model = models.tbl_sinkronisasi_kebijakan_psm
    success_url = reverse_lazy("pelaporan_tbl_sinkronisasi_kebijakan_psm_list")


class tbl_tes_urine_deteksi_dini_pelaksanaan_psmListView(generic.ListView):
    model = models.tbl_tes_urine_deteksi_dini_pelaksanaan_psm
    form_class = forms.tbl_tes_urine_deteksi_dini_pelaksanaan_psmForm


class tbl_tes_urine_deteksi_dini_pelaksanaan_psmCreateView(generic.CreateView):
    model = models.tbl_tes_urine_deteksi_dini_pelaksanaan_psm
    form_class = forms.tbl_tes_urine_deteksi_dini_pelaksanaan_psmForm


class tbl_tes_urine_deteksi_dini_pelaksanaan_psmDetailView(generic.DetailView):
    model = models.tbl_tes_urine_deteksi_dini_pelaksanaan_psm
    form_class = forms.tbl_tes_urine_deteksi_dini_pelaksanaan_psmForm


class tbl_tes_urine_deteksi_dini_pelaksanaan_psmUpdateView(generic.UpdateView):
    model = models.tbl_tes_urine_deteksi_dini_pelaksanaan_psm
    form_class = forms.tbl_tes_urine_deteksi_dini_pelaksanaan_psmForm
    pk_url_kwarg = "pk"


class tbl_tes_urine_deteksi_dini_pelaksanaan_psmDeleteView(generic.DeleteView):
    model = models.tbl_tes_urine_deteksi_dini_pelaksanaan_psm
    success_url = reverse_lazy(
        "pelaporan_tbl_tes_urine_deteksi_dini_pelaksanaan_psm_list"
    )


class tbl_tes_urine_deteksi_dini_psmListView(generic.ListView):
    model = models.tbl_tes_urine_deteksi_dini_psm
    form_class = forms.tbl_tes_urine_deteksi_dini_psmForm


class tbl_tes_urine_deteksi_dini_psmCreateView(generic.CreateView):
    model = models.tbl_tes_urine_deteksi_dini_psm
    form_class = forms.tbl_tes_urine_deteksi_dini_psmForm


class tbl_tes_urine_deteksi_dini_psmDetailView(generic.DetailView):
    model = models.tbl_tes_urine_deteksi_dini_psm
    form_class = forms.tbl_tes_urine_deteksi_dini_psmForm


class tbl_tes_urine_deteksi_dini_psmUpdateView(generic.UpdateView):
    model = models.tbl_tes_urine_deteksi_dini_psm
    form_class = forms.tbl_tes_urine_deteksi_dini_psmForm
    pk_url_kwarg = "pk"


class tbl_tes_urine_deteksi_dini_psmDeleteView(generic.DeleteView):
    model = models.tbl_tes_urine_deteksi_dini_psm
    success_url = reverse_lazy("pelaporan_tbl_tes_urine_deteksi_dini_psm_list")


class tbl_workshop_penggiat_pelaksanaan_psmListView(generic.ListView):
    model = models.tbl_workshop_penggiat_pelaksanaan_psm
    form_class = forms.tbl_workshop_penggiat_pelaksanaan_psmForm


class tbl_workshop_penggiat_pelaksanaan_psmCreateView(generic.CreateView):
    model = models.tbl_workshop_penggiat_pelaksanaan_psm
    form_class = forms.tbl_workshop_penggiat_pelaksanaan_psmForm


class tbl_workshop_penggiat_pelaksanaan_psmDetailView(generic.DetailView):
    model = models.tbl_workshop_penggiat_pelaksanaan_psm
    form_class = forms.tbl_workshop_penggiat_pelaksanaan_psmForm


class tbl_workshop_penggiat_pelaksanaan_psmUpdateView(generic.UpdateView):
    model = models.tbl_workshop_penggiat_pelaksanaan_psm
    form_class = forms.tbl_workshop_penggiat_pelaksanaan_psmForm
    pk_url_kwarg = "pk"


class tbl_workshop_penggiat_pelaksanaan_psmDeleteView(generic.DeleteView):
    model = models.tbl_workshop_penggiat_pelaksanaan_psm
    success_url = reverse_lazy("pelaporan_tbl_workshop_penggiat_pelaksanaan_psm_list")


class tbl_workshop_penggiat_psmListView(generic.ListView):
    model = models.tbl_workshop_penggiat_psm
    form_class = forms.tbl_workshop_penggiat_psmForm


class tbl_workshop_penggiat_psmCreateView(generic.CreateView):
    model = models.tbl_workshop_penggiat_psm
    form_class = forms.tbl_workshop_penggiat_psmForm


class tbl_workshop_penggiat_psmDetailView(generic.DetailView):
    model = models.tbl_workshop_penggiat_psm
    form_class = forms.tbl_workshop_penggiat_psmForm


class tbl_workshop_penggiat_psmUpdateView(generic.UpdateView):
    model = models.tbl_workshop_penggiat_psm
    form_class = forms.tbl_workshop_penggiat_psmForm
    pk_url_kwarg = "pk"


class tbl_workshop_penggiat_psmDeleteView(generic.DeleteView):
    model = models.tbl_workshop_penggiat_psm
    success_url = reverse_lazy("pelaporan_tbl_workshop_penggiat_psm_list")


class tbl_workshop_tematik_pelaksanaan_psmListView(generic.ListView):
    model = models.tbl_workshop_tematik_pelaksanaan_psm
    form_class = forms.tbl_workshop_tematik_pelaksanaan_psmForm


class tbl_workshop_tematik_pelaksanaan_psmCreateView(generic.CreateView):
    model = models.tbl_workshop_tematik_pelaksanaan_psm
    form_class = forms.tbl_workshop_tematik_pelaksanaan_psmForm


class tbl_workshop_tematik_pelaksanaan_psmDetailView(generic.DetailView):
    model = models.tbl_workshop_tematik_pelaksanaan_psm
    form_class = forms.tbl_workshop_tematik_pelaksanaan_psmForm


class tbl_workshop_tematik_pelaksanaan_psmUpdateView(generic.UpdateView):
    model = models.tbl_workshop_tematik_pelaksanaan_psm
    form_class = forms.tbl_workshop_tematik_pelaksanaan_psmForm
    pk_url_kwarg = "pk"


class tbl_workshop_tematik_pelaksanaan_psmDeleteView(generic.DeleteView):
    model = models.tbl_workshop_tematik_pelaksanaan_psm
    success_url = reverse_lazy("pelaporan_tbl_workshop_tematik_pelaksanaan_psm_list")


class tbl_workshop_tematik_psmListView(generic.ListView):
    model = models.tbl_workshop_tematik_psm
    form_class = forms.tbl_workshop_tematik_psmForm


class tbl_workshop_tematik_psmCreateView(generic.CreateView):
    model = models.tbl_workshop_tematik_psm
    form_class = forms.tbl_workshop_tematik_psmForm


class tbl_workshop_tematik_psmDetailView(generic.DetailView):
    model = models.tbl_workshop_tematik_psm
    form_class = forms.tbl_workshop_tematik_psmForm


class tbl_workshop_tematik_psmUpdateView(generic.UpdateView):
    model = models.tbl_workshop_tematik_psm
    form_class = forms.tbl_workshop_tematik_psmForm
    pk_url_kwarg = "pk"


class tbl_workshop_tematik_psmDeleteView(generic.DeleteView):
    model = models.tbl_workshop_tematik_psm
    success_url = reverse_lazy("pelaporan_tbl_workshop_tematik_psm_list")
