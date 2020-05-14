from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    codigo = models.IntegerField

    def __str__(self):
        return '{}'.format(self.nombre,self.codigo)
        