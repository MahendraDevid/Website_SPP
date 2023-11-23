from django import forms
from .models import Petugas

class PetugasForm(forms.ModelForm):
    class Meta:
        model = Petugas
        exclude = ['id_petugas']  # Kegecualikan id_petugas dari form
