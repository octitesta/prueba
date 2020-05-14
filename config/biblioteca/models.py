from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    codigo = models.AutoField(primary_key=True)
    def __str__(self):
        return '{} {}'.format(self.nombre,self.codigo)


class Libro(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    editorial = models.CharField(max_length=30)
    paginas = models.IntegerField()
    def __str__(self):
        return '{} {}'.format(self.codigo,self.titulo)

