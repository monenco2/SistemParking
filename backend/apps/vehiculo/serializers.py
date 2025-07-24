from rest_framework import serializers
from .models import *


class VehiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehiculo
        fields = ('__all__')