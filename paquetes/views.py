from rest_framework import viewsets

from .models import Paquete
from .serializers import PaqueteSerializer

# Create your views here.

class PaqueteVieSet(viewsets.ModelViewSet):
    queryset = Paquete.objects.all()
    serializer_class = PaqueteSerializer


