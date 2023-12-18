from django.db import models

class Cliente(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
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
        ('Pendiente', 'Pendiente'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
    )

    idusuario = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    latitud = models.DecimalField(max_digits=18, decimal_places=15)
    longitud = models.DecimalField(max_digits=18, decimal_places=15)
    descripcion = models.TextField()
    tipoIncidente = models.CharField(max_length=80)
    nivelPeligro = models.CharField(max_length=80)
    estado = models.CharField(max_length=9, choices=ESTADO_CHOICES, default='Pendiente')
    fechaCreacion = models.DateTimeField(auto_now_add=True)

class CallePeligrosas(models.Model):
    nombre = models.CharField(max_length=255)
    latitud = models.DecimalField(max_digits=40, decimal_places=8)
    longitud = models.DecimalField(max_digits=40, decimal_places=8)
    descripcion = models.TextField()
    nivelPeligro = models.IntegerField()

    
    
