from .models import Paquete
from rest_framework import serializers

class PaqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paquete
        fields = ('destino', 'descripcion', 'precio', 'gia', 'fechaPartida','img_url')