from django.db import models
from django.contrib.auth.models import User

class Estados_tablero(models.Model):
    nombre= models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Tablero(models.Model):
    nombre_tablero=models.CharField(max_length=255)
    id_creador=models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    estado=models.OneToOneField(Estados_tablero,on_delete=models.CASCADE)

class Estados_idea(models.Model):
    nombre = models.CharField(max_length=50)

class Ideas(models.Model):
    mensaje=models.TextField()
    estado=models.OneToOneField(Estados_tablero,related_name='posts', on_delete=models.CASCADE)
    id_creador=models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    id_tablero=models.ForeignKey(Tablero,null=True, blank=True, on_delete=models.CASCADE)

