from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class tbl_responden_surveiListView(generic.ListView):
    model = models.tbl_responden_survei
    form_class = forms.tbl_responden_surveiForm


class tbl_responden_surveiCreateView(generic.CreateView):
    model = models.tbl_responden_survei
    form_class = forms.tbl_responden_surveiForm


class tbl_responden_surveiDetailView(generic.DetailView):
    model = models.tbl_responden_survei
    form_class = forms.tbl_responden_surveiForm


class tbl_responden_surveiUpdateView(generic.UpdateView):
    model = models.tbl_responden_survei
    form_class = forms.tbl_responden_surveiForm
    pk_url_kwarg = "pk"


class tbl_responden_surveiDeleteView(generic.DeleteView):
    model = models.tbl_responden_survei
    success_url = reverse_lazy("survei_tbl_responden_survei_list")


class tbl_surveiListView(generic.ListView):
    model = models.tbl_survei
    form_class = forms.tbl_surveiForm


class tbl_surveiCreateView(generic.CreateView):
    model = models.tbl_survei
    form_class = forms.tbl_surveiForm


class tbl_surveiDetailView(generic.DetailView):
    model = models.tbl_survei
    form_class = forms.tbl_surveiForm


class tbl_surveiUpdateView(generic.UpdateView):
    model = models.tbl_survei
    form_class = forms.tbl_surveiForm
    pk_url_kwarg = "pk"


class tbl_surveiDeleteView(generic.DeleteView):
    model = models.tbl_survei
    success_url = reverse_lazy("survei_tbl_survei_list")