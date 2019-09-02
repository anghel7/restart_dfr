from django.db import models

# Create your models here.
class Paquete(models.Model):
    destino = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField()
    gia = models.CharField(max_length=100)
    fechaPartida = models.CharField(max_length=100)
    img_url = models.CharField(max_length=500)