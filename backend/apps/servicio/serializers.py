from rest_framework import serializers
from .models import *


class ServicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servicio
        fields = ('__all__')