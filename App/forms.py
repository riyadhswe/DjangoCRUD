from django import forms
from App import models


class student_form(forms.ModelForm):
    class Meta:
        model = models.student_model
        fields = "__all__"
