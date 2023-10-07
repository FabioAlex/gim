from django.db import models

# Create your models here.


class Docente(models.Model):
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    asignatura_id = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)

class Estudiante(models.Model):
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=200)
    documento = models.CharField(max_length=20)
    fecha_admision = models.DateField()

class Asignatura(models.Model):
    nombre = models.TextField()
    grado_id = models.IntegerField()
    docente_id = models.IntegerField()
    descripcion = models.TextField()

class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)
    # Agrega otros campos según tus necesidades