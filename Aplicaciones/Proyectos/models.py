from django.db import models

# Create your models here.
class Desarrollador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        fila = "{0}: {1} {2} {3}"
        return fila.format(self.id, self.nombre, self.apellido, self.especialidad)
    
    
class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    responsable = models.ForeignKey(Desarrollador, on_delete=models.CASCADE)
    
    
    def __str__(self):
        fila = "{0}: {1} {2} {3} {4}"
        return fila.format(self.id, self.nombre, self.descripcion, self.fecha_inicio,self.responsable)