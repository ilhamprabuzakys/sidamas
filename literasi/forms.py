from django import forms
from . import models


class LiterasiForm(forms.ModelForm):
    class Meta:
        model = models.Literasi
        fields = [
            "created_by",
            "updated_by",
            "dokumen",
            "Judul",
        ]
