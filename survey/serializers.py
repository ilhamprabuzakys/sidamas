from rest_framework import serializers
from django.contrib.auth.models import User

from . import models

class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')

class survey(serializers.ModelSerializer):
    pemilik = ChoiceField(choices=models.survey.PEMILIK_CHOICES)
    status = ChoiceField(choices=models.survey.STATUS_CHOICES)
    dibuat_oleh = CurrentUserSerializer(many=False)
    created= serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = models.survey
        read_only_fields = ["created"]
        fields = [
            "judul",
            "jsontext",
            "status",
            "pemilik",
            "dibuat_oleh",
            "created",
        ]

class survey_create(serializers.ModelSerializer):
    class Meta:
        model = models.survey
        read_only_fields = ["created"]
        fields = [
            "judul",
            "jsontext",
            "status",
            "pemilik",
            "dibuat_oleh",
            "created",
        ]
class surveyshort(serializers.ModelSerializer):
    class Meta:
        model = models.surveyshort
        fields = [
            "satker",
            "shortcode",
            "survey",
            "dibuat_oleh",
            "created",
            "status"
        ]

class survey_result(serializers.ModelSerializer):
    class Meta:
        model = models.survey_result
        fields = [
            "survey",
            "shortcode",
            "hasil",
            "dibuat_oleh",
            "created",
        ]

