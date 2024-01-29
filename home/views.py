import json
from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views import View
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin
from django.views.generic import TemplateView

from .authbe import SidamasLDAPBackend
from berita.models import Berita

from literasi.models import Literasi

class BerandaView(View):
    template_name = "home/beranda.html"
    
    def get(self, request):
        data = Berita.objects.all()
        
        context = { "data": data }
        return render(request, self.template_name, context)

class SurveiView(View):
    template_name = "home/survei.html"
    
    def get(self, request):
        if self.request.GET.get('tipe') == 'skm':
            daftarPertanyaan = [
                {
                    "pertanyaan" : "Apakah Saudara memenuhi kriteria persyaratan untuk mengikuti pelatihan?",
                    "jawaban" : [
                        {"opsi" : "Tidak Setuju" , "nilai" : "1"},
                        {"opsi" : "Kurang Setuju" , "nilai" : "2"},
                        {"opsi" : "Setuju" , "nilai" : "3"},
                        {"opsi" : "Sangat Setuju" , "nilai" : "4"}
                    ]
                },
                {
                    "pertanyaan" : "Apakah tahapan pelatiha yang diberikan dapat dipahami?",
                    "jawaban" : [
                        {"opsi" : "Tidak Paham" , "nilai" : "1"},
                        {"opsi" : "Kurang Paham" , "nilai" : "2"},
                        {"opsi" : "Paham" , "nilai" : "3"},
                        {"opsi" : "Sangat Paham" , "nilai" : "4"}
                    ]
                },
                {
                    "pertanyaan" : "Apakah waktu pelaihan (3 hari) telah mencukupi dalam menambah keterampilan?",
                    "jawaban" : [
                        {"opsi" : "Sangat Tidak Cukup" , "nilai" : "1"},
                        {"opsi" : "Tidak Cukup" , "nilai" : "2"},
                        {"opsi" : "Cukup" , "nilai" : "3"},
                        {"opsi" : "Sangat Cukup" , "nilai" : "4"}
                    ]
                },
                {
                    "pertanyaan" : "Apakah Uang transport yang diberikan mencukupi sebagai pengganti transport Saudara?",
                    "jawaban" : [
                        {"opsi" : "Sangat Tidak Cukup" , "nilai" : "1"},
                        {"opsi" : "Tidak Cukup" , "nilai" : "2"},
                        {"opsi" : "Cukup" , "nilai" : "3"},
                        {"opsi" : "Sangat Cukup" , "nilai" : "4"}
                    ]
                },
                {
                    "pertanyaan" : "Apakah dengan Pelatihan ini Saudara mampu menghasilkan produk sesuai yang dilatihkan?",
                    "jawaban" : [
                        {"opsi" : "Tidak Mampu" , "nilai" : "1"},
                        {"opsi" : "Kurang Mampu" , "nilai" : "2"},
                        {"opsi" : "Mampu" , "nilai" : "3"},
                        {"opsi" : "Sangat Mampu" , "nilai" : "4"}
                    ]
                },
                {
                    "pertanyaan" : "Bagaimana Kemampuan Insruktur dalam memberikan maeri dan praktek pelatihan?",
                    "jawaban" : [
                        {"opsi" : "Tidak Kompoten" , "nilai" : "1"},
                        {"opsi" : "Kurang Kompoten" , "nilai" : "2"},
                        {"opsi" : "Kompoten" , "nilai" : "3"},
                        {"opsi" : "Sangat Kompoten" , "nilai" : "4"}
                    ]
                },
                {
                    "pertanyaan" : "Bagaimana Sikap Simpatik Pelaksana Kegiatan dalam memberikan pelatihan?",
                    "jawaban" : [
                        {"opsi" : "Tidak Simpatik" , "nilai" : "1"},
                        {"opsi" : "Kurang Simpatik" , "nilai" : "2"},
                        {"opsi" : "Simpatik" , "nilai" : "3"},
                        {"opsi" : "Sangat Simpatik" , "nilai" : "4"}
                    ]
                },
                {
                    "pertanyaan" : "Bagaimana Sikap Pelaksana Kegiatan dalam memberikan pelatihan?",
                    "jawaban" : [
                        {"opsi" : "Tidak Peduli" , "nilai" : "1"},
                        {"opsi" : "Kurang Peduli" , "nilai" : "2"},
                        {"opsi" : "Peduli" , "nilai" : "3"},
                        {"opsi" : "Sangat Peduli" , "nilai" : "4"}
                    ]
                },
                {
                    "pertanyaan" : "Apakah sarana dan prasarana pelatihan telah memadai dalam pelaksanaan pelatihan?",
                    "jawaban" : [
                        {"opsi" : "Tidak Memadai" , "nilai" : "1"},
                        {"opsi" : "Kurang Memadai" , "nilai" : "2"},
                        {"opsi" : "Memadai" , "nilai" : "3"},
                        {"opsi" : "Sangat Memadai" , "nilai" : "4"}
                    ]
                }
            ]
        else:
            daftarPertanyaan = [
                {
                    "pertanyaan":
                        "Bagaimana pendapat Saudara tentang kesesuaian persyaratan pelayanan dengan jenis pelayanannya?",
                    "jawaban": [
                        { "opsi": "Tidak sesuai", "nilai": "1" },
                        { "opsi": "Kurang sesuai", "nilai": "2" },
                        { "opsi": "Sesuai", "nilai": "3" },
                        { "opsi": "Sangat sesuai", "nilai": "4" },
                    ],
                },
                {
                    "pertanyaan":
                        "Bagaimana pemahaman Saudara tentang kemudahan prosedur pelayanan yang diberikan?",
                    "jawaban": [
                        { "opsi": "Tidak paham", "nilai": "1" },
                        { "opsi": "Kurang paham", "nilai": "2" },
                        { "opsi": "Paham", "nilai": "3" },
                        { "opsi": "Sangat paham", "nilai": "4" },
                    ],
                },
                {
                    "pertanyaan":
                        "Bagaimana pendapat Saudara tentang kecepatan waktu dalam memberikan pelayanan?",
                    "jawaban": [
                        { "opsi": "Tidak cepat", "nilai": "1" },
                        { "opsi": "Kurang cepat", "nilai": "2" },
                        { "opsi": "Cepat", "nilai": "3" },
                        { "opsi": "Sangat cepat", "nilai": "4" },
                    ],
                },
                {
                    "pertanyaan":
                        "Bagaimana pendapat Saudara tentang kewajaran biaya/tarif dalam pelayanan?",
                    "jawaban": [
                        { "opsi": "Sangat mahal", "nilai": "1" },
                        { "opsi": "Cukup mahal", "nilai": "2" },
                        { "opsi": "Murah", "nilai": "3" },
                        { "opsi": "Gratis", "nilai": "4" },
                    ],
                },
                {
                    "pertanyaan":
                        "Petugas tidak pernah meminta imbalan dan melakukan pungutan liar?",
                    "jawaban": [
                        { "opsi": "Tidak setuju", "nilai": "1" },
                        { "opsi": "Kurang setuju", "nilai": "2" },
                        { "opsi": "Setuju", "nilai": "3" },
                        { "opsi": "Sangat Setuju", "nilai": "4" },
                    ],
                },
                {
                    "pertanyaan":
                        "Bagaimana pendapat Saudara tentang kesesuaian produk pelayanan antara yang tercantum dalam standar pelayanan dengan hasil yang diberikan?",
                    "jawaban": [
                        { "opsi": "Tidak sesuai", "nilai": "1" },
                        { "opsi": "Kurang sesuai", "nilai": "2" },
                        { "opsi": "Sesuai", "nilai": "3" },
                        { "opsi": "Sangat sesuai", "nilai": "4" },
                    ],
                },
                {
                    "pertanyaan":
                        "Bagaimana pendapat Saudara tentang kompetensi/kemampuan petugas dalam pelayanan?",
                    "jawaban": [
                        { "opsi": "Tidak kompeten", "nilai": "1" },
                        { "opsi": "Kurang kompeten", "nilai": "2" },
                        { "opsi": "Kompeten", "nilai": "3" },
                        { "opsi": "Sangat kompeten", "nilai": "4" },
                    ],
                },
                {
                    "pertanyaan":
                        "Bagaimana pendapat Saudara tentang perilaku petugas dalam pelayanan terkait kesopanan dan keramahan?",
                    "jawaban": [
                        { "opsi": "Tidak sopan dan ramah", "nilai": "1" },
                        { "opsi": "Kurang sopan dan ramah", "nilai": "2" },
                        { "opsi": "Sopan dan ramah", "nilai": "3" },
                        { "opsi": "Sangat sopan dan ramah", "nilai": "4" },
                    ],
                },
                {
                    "pertanyaan":
                        "Bagaimana pendapat Saudara tentang penanganan pengaduan pengguna layanan?",
                    "jawaban": [
                        { "opsi": "Tidak ada", "nilai": "1" },
                        { "opsi": "Ada tetapi tidak berfungsi", "nilai": "2" },
                        { "opsi": "Berfungsi kurang maksimal", "nilai": "3" },
                        { "opsi": "Dikelola dengan baik", "nilai": "4" },
                    ],
                },
                {
                    "pertanyaan":
                        "Bagaimana pendapat Saudara tentang kualitas sarana dan prasarana?",
                    "jawaban": [
                        { "opsi": "Buruk", "nilai": "1" },
                        { "opsi": "Cukup", "nilai": "2" },
                        { "opsi": "Baik", "nilai": "3" },
                        { "opsi": "Sangat baik", "nilai": "4" },
                    ],
                },
            ]
            
        data = json.dumps(daftarPertanyaan, ensure_ascii=False)

        context = {
            "data": data
        }
    
        return render(request, self.template_name, context)

class MediaSosialView(TemplateView):
    template_name = "home/media_sosial.html"

class LiterasiView(View):
    template_name = "home/literasi.html"
    
    def get(self, request):
        daftar_literasi = Literasi.objects.all()
        #print(daftar_literasi)
        return render(request, self.template_name, { 'daftar_literasi' : daftar_literasi })

@xframe_options_sameorigin
def literasi_view(request):
        template_name = "home/literasi.html"
        daftar_literasi = Literasi.objects.all()
        #print(daftar_literasi)
        return render(request, template_name, { 'daftar_literasi' : daftar_literasi })

class BerandaKegiatanView(TemplateView):
    template_name = "home/beranda_kegiatan.html"

    # def get(self, request):
    #     return render(request, self.template_name)

class BeritaView(View):
    template_name = "home/berita.html"
    
    def get(self, request):
        return render(request, self.template_name)
        
class BeritaDetailView(View):
    template_name = "home/detail_berita.html"
    
    def get(self, request, slug):
        semua_berita = Berita.objects.all()
        data = Berita.objects.get(slug=slug)
        user_pembuat = data.created_by

        tags_list = [tag.lstrip("#\ufeff") for tag in data.tags.split()]
        
        current_index = semua_berita.filter(slug=slug).first().pk
        total_berita = semua_berita.count()

        prev_index = current_index - 1 if current_index > 1 else None
        next_index = current_index + 1 if current_index < total_berita else None

        berita_sebelumnya = semua_berita.filter(pk=prev_index).first()
        berita_selanjutnya = semua_berita.filter(pk=next_index).first()
        
        context = {
            "id" : data.pk,
            "slug" : data.slug,
            "judul": data.judul,
            "kategori": data.kategori,
            "created": data.created_at,
            "last_updated": data.updated_at,
            "isi_berita": data.isi_berita,
            "tanggal": data.tanggal,
            "status": data.status,
            "tags": data.tags,
            "tags_list": tags_list,
            "gambar_utama": data.gambar_utama,
            "created_by": data.created_by,
            "updated_by": data.updated_by,
            "kategori_id": data.kategori,
            "semua_berita": semua_berita,
            "berita_sebelumnya": berita_sebelumnya,
            "berita_selanjutnya": berita_selanjutnya,
            "author": user_pembuat
        }
        
        return render(request, self.template_name, context=context)
    
    
def truncate_and_escape(text, max_words):
    """
    Escape HTML and truncate text to a maximum number of words.
    This is a helper function like a Django bleach
    """
    words = text.split(' ')
    if len(words) > max_words:
        truncated_text = ' '.join(words[:max_words]) + '...'
    else:
        truncated_text = ' '.join(words)

    truncated_text = truncated_text.lstrip('<p>').rstrip('</p>')

    return mark_safe(escape(truncated_text))

# Redirecting user
def redirect_user_to_login(request):
    return redirect(reverse('login'))

@method_decorator(require_http_methods(["GET", "POST"]), name='dispatch')
class LoginView(View):
    template_name = "auth/login.html"
    redirect_authenticated_user = True

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Masukan yang Anda berikan tidak valid. Harap periksa kembali.')
        return response
    
    def get_success_url(self):
        data_user = self.request.user
        data_user_profile = data_user.profile
        
        print(f'User {data_user} berhasil login ...')
        
        if data_user_profile is None:
            logout()
            return HttpResponseForbidden("Terjadi kesalahan, tolong login ulang.")
        
        print('Data user profile :', data_user_profile)
        
        satker_value = getattr(data_user_profile, 'satker', None)
        role_value = getattr(data_user_profile, 'role', None)
        
        print('Data user satker: ', satker_value)
        print('Data user direktorat: ', role_value)
        
        next_url = self.request.GET.get('next', None)
        
        if satker_value is None:
            return reverse("dashboard:profile")
        elif role_value is None:
            return reverse("pilih_direktorat")
        elif satker_value and role_value:
            if next_url:
                return next_url
            else:
                return reverse("dashboard:index")