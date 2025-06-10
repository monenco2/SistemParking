from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.TextField("nombre")
    apellido = models.TextField("apellido")
    rol_id = models.TextField("rol")

    def __str__ (self):
            return f'{self.apellido}'