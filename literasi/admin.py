from django.contrib import admin
from django import forms

from . import models


class LiterasiAdminForm(forms.ModelForm):

    class Meta:
        model = models.Literasi
        fields = "__all__"


class LiterasiAdmin(admin.ModelAdmin):
    form = LiterasiAdminForm
    list_display = [
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "dokumen",
            "Judul",
            "status",
            "kategori",
            "tags",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]


admin.site.register(models.Literasi, LiterasiAdmin)
