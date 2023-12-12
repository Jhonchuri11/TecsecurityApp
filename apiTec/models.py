from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    numero = models.CharField(max_length=9)
    password = models.CharField(max_length=255)

class Comentario(models.Model):
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    comentario = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)

class Incidentes(models.Model):

    ESTADO_CHOICES = (
        ('P', 'Pendiente'),
        ('A', 'Aprobado'),
        ('R', 'Rechazado'),
    )
    TIPO_INCIDENTE_CHOICES = (
        ('I', 'Incendio'),
        ('F', 'Fuga de gas'),
        ('O', 'Accidente de tránsito'),
    )

    NIVEL_PELIGRO_CHOICES = (
        ('B', 'Bajo'),
        ('M', 'Moderado'),
        ('A', 'Alto'),
    )
    idusuario = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    latitud = models.DecimalField(max_digits=10, decimal_places=8)
    longitud = models.DecimalField(max_digits=11, decimal_places=8)
    descripcion = models.TextField()
    tipoIncidente = models.CharField(max_length=1, choices=TIPO_INCIDENTE_CHOICES, default='I')
    nivelPeligro = models.CharField(max_length=1, choices=NIVEL_PELIGRO_CHOICES, blank=True, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='P')
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        
        if self.tipoIncidente == 'I':
            self.nivelPeligro = 'A'  
        elif self.tipoIncidente == 'F':
            self.nivelPeligro = 'M'  
        else:
            self.nivelPeligro = 'B'

        super().save(*args, **kwargs)

class CallePeligrosas(models.Model):
    nombre = models.CharField(max_length=255)
    latitud = models.DecimalField(max_digits=10, decimal_places=8)
    longitud = models.DecimalField(max_digits=11, decimal_places=8)
    descripcion = models.TextField()
    nivelPeligro = models.IntegerField()

    
    
