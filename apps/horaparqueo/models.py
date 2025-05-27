from django.db import models

# Create your models here.
class Horaparqueo(models.model):
    precio = models.TextField("precio")
    servicio_id = models.TextField("servicio")
