from django import forms
from djapp.models import Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
