from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View, generic
from django.urls import reverse, reverse_lazy

from survei.models import DataSurvei, TipeSurvei
from . import models
from . import forms
from users.models import Profile
import json
import random
import string
import json
from django.http import HttpResponse, HttpResponseRedirect

class GlobalPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser == False and request.user.is_staff == False and request.user.profile.role is None or request.user.profile.satker is None or request.user.profile.is_verified == False:
            user = self.request.user
            message = "Maaf " + user.username + ", anda tidak memiliki hak akses untuk mengunjungi halaman ini."
            print(message)
            return HttpResponseRedirect(reverse("dashboard:profile"))
        return super().dispatch(request, *args, **kwargs)
    
class SurveyBaseView(GlobalPermissionMixin, LoginRequiredMixin):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
# Punya Bapak
def create_unique_id():
    return ''.join(random.choices(string.ascii_uppercase+string.digits, k=8))

def create_shortcode():
    id = create_unique_id()
    unique = False
    while not unique:
        print(id)
        try:
            if not models.shortcode.objects.get(code=id):
                unique = True
            else:
                id = create_unique_id()
        except:
            id = create_unique_id()
            unique = True
    models.shortcode.objects.create(code=id)
    return id

def create_sc(request, id):
    survey = models.survey.objects.get(pk=id)
    pemilik = request.user
    profil = Profile.objects.get(user=pemilik)
    sc = create_shortcode()
    short = models.surveyshort(satker=profil.satker, shortcode=sc, dibuat_oleh=pemilik,status='1',survey=survey)
    short.save()
    return HttpResponse(json.dumps({'shortcode':sc}), content_type='application/json')

class PWAView(View):
    def get(self, request):
        return render(request, "pages/eform.html")

class eFormView(View):
    def get(self, request):
        context = {'bc': [{'text':'Home','url':'/dashboard/'},{'text':'E-Form','url':'/survey/eform/'}]}
        return render(request, "pages/eform.html", context)

class eFormShortView(View):
    def get(self, request):
        return render(request, "pages/eform_shortcode.html")

class eFormGoSurveyView(View):
    def get(self, request,id):
        try:
            sc = models.surveyshort.objects.get(shortcode=id)
            survey = models.survey.objects.get(pk=sc.survey.id)
            context = {"survey_source": survey.jsontext, "id":id}
        except:
            context = {"survey_source": json.dumps({"title":"Kode Survey Keliru","pages": [{"name": "page1"}]}), "id":id}
        return render(request, "pages/go_survey.html",context)

class eFormCreateView(View):
    def get(self, request):
        return render(request, "pages/eform_create.html")

class eFormEditView(View):
    def get(self, request, id):
        survey = models.survey.objects.get(pk=id)
        context = {"survey_source": survey.jsontext, "id":id}
        print(context)
        return render(request, "pages/eform_edit.html", context)

# Punya custom
class FormulirElektronikView(SurveyBaseView, View):
    template_name = "formulir_elektronik/formulir_elektronik.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
class FormulirElektronikCreateView(SurveyBaseView, View):
    template_name = "formulir_elektronik/create.html"
    
    def get(self, request):
        return render(request, self.template_name)

class FormulirElektronikEditView(SurveyBaseView, View):
    template_name = "formulir_elektronik/edit.html"

    def get(self, request, id):
        survey = models.survey.objects.get(pk=id)
        context = {"survey_source": survey.jsontext, "id":id, "title":survey.judul}
        return render(request, self.template_name, context)

# PSM
class SKMTesUrineView(SurveyBaseView, View):
    template_name = "psm/skm_tes_urine/skm_tes_urine.html"
    
    def get(self, request):
        tipe_survei = TipeSurvei.objects.get(nama="SKM Tes Urine")
        
        list_survei = DataSurvei.objects.filter(tipe=tipe_survei.id)
        
        context = {
            'list_survei': list_survei,
            'tipe_survei': tipe_survei.id
        }
        
        return render(request, self.template_name, context)

# Dayatif
class SKMLifeSkill(SurveyBaseView, View):
    template_name = "dayatif/skm_life_skill/skm_life_skill.html"
    
    def get(self, request):
        return render(request, self.template_name)

class KeberhasilanKewirausahaanView(SurveyBaseView, View):
    template_name = "dayatif/keberhasilan_kewirausahaan/keberhasilan_kewirausahaan.html"
    
    def get(self, request):
        return render(request, self.template_name)