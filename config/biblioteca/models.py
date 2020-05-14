from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    codigo = models.AutoField(primary_key=True)
    def __str__(self):
        return '{}'.format(self.nombre)


class Libro(models.Model):
    codigo = models.AutoField(primary_key=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    editorial = models.CharField(max_length=30)
    paginas = models.IntegerField()
    def __str__(self):
        return '{}'.format(self.titulo)


class Ejemplar(models.Model):
    codigo = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    localizacion = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.libro)

class Usuario(models.Model):    
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    ejemplares = models.ManyToManyField(Ejemplar)
    def __str__(self):
        return '{}'.format(self.nombre)