from django.db import models

class SPP(models.Model):
    id_spp = models.IntegerField(primary_key=True)  # id_spp sebagai primary key
    tahun = models.IntegerField()
    nominal = models.IntegerField()
