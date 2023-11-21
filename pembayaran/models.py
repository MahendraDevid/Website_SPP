from django.db import models

class Pembayaran(models.Model):
    id_pembayaran = models.IntegerField(primary_key=True)
    nisn = models.CharField(max_length=10)
    tgl_bayar = models.DateField()
    bulan_dibayar = models.CharField(max_length=8)
    tahun_dibayar = models.CharField(max_length=4)
    jumlah_bayar = models.IntegerField()
    
    # Ubah ini menjadi ForeignKey dengan string
    id_petugas = models.ForeignKey('petugas.Petugas', on_delete=models.CASCADE)
    id_spp = models.ForeignKey('spp.SPP', on_delete=models.CASCADE)
