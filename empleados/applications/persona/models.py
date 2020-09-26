from django.db import models
from empleados.applications.departamento.models import Departamento

# Create your models here.


class Empleado(models.Model):
    """
        Modelo para tabla 'Empleado'
    """
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro tipo')
    )
    first_name = models.CharField('Nombre', max_length=20)
    last_name = models.CharField('Apellidos', max_length=60)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField('Foto', upload_to=None, height_field=None, width_field=None)

    def __str__(self):
        return '{}, {} - {}'.format(self.first_name, self.last_name, self.job)
