from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.TextField("nombre", blank=True )
    apellido = models.TextField("apellido", blank=True)
    email = models.TextField("email", blank=True)
    password = models.TextField("password", blank=True)
    rol_id = models.TextField("rol", null=True)

    def __str__(self):
        return f'{self.apellido}'