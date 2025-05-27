from django.db import models

# Create your models here.
class Servicio(models.model):
    nombre = models.TextField("nombre")
    