from rest_framework import serializers
from .models import *


class HoraparqueoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Horaparqueo
        fields = ('__all__')