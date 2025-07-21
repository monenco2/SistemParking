from rest_framework import serializers
from .models import *


class pagofinalSerializer(serializers.ModelSerializer):

    class Meta:
        model = pagofinal
        fields = ('__all__')