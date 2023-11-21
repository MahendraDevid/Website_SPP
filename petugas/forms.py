from django import forms
from .models import Petugas

class PetugasForm(forms.ModelForm):
    class Meta:
        model = Petugas
        fields = ['id_petugas', 'username', 'password', 'nama_petugas', 'level']
