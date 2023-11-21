from django.shortcuts import render, redirect, get_object_or_404
from .models import Petugas
from .forms import PetugasForm

def daftar_petugas(request):
    petugas_list = Petugas.objects.all()  
    return render(request, 'petugas/daftar_petugas.html', {'petugas_list': petugas_list})

def tambah_petugas(request):
    if request.method == 'POST':
        form = PetugasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_petugas')
    else:
        form = PetugasForm()
    
    return render(request, 'petugas/tambah_petugas.html', {'form': form})

def detail_petugas(request, petugas_id):
    petugas = get_object_or_404(Petugas, pk=petugas_id)  
    return render(request, 'petugas/detail_petugas.html', {'petugas': petugas})

def edit_petugas(request, petugas_id):
    petugas = get_object_or_404(Petugas, pk=petugas_id)
    if request.method == 'POST':
        form = PetugasForm(request.POST, instance=petugas)
        if form.is_valid():
            form.save()
            return redirect('daftar_petugas')
    else:
        form = PetugasForm(instance=petugas)
    
    return render(request, 'petugas/edit_petugas.html', {'form': form})

def hapus_petugas(request, petugas_id):
    petugas = get_object_or_404(Petugas, pk=petugas_id)
    petugas.delete()
    return redirect('daftar_petugas')
