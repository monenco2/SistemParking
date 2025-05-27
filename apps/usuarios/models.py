from django.db import models

# Create your models here.
class Usuarios(models.model):
    nombre = models.TextField("nombre")
    apellido = models.TextField("apellido")
    rol_id = models.TextField("rol")