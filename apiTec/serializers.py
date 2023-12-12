from rest_framework import serializers
from .models import Comentario, Incidentes, CallePeligrosas, Cliente, Like
import hashlib

# Serializando el cliente = user
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'email', 'numero', 'password']
    # Funcion que encripta el password ingresado por el user
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            validated_data['password'] = hashed_password

        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
    
class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['idcliente','comentario', 'fechaCreacion']

class likeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class IncidentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidentes
        fields = ['id','idusuario','latitud','longitud','descripcion','tipoIncidente','nivelPeligro','estado','fechaCreacion']

class CallesPeligrosaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallePeligrosas
        fields = ['id','nombre','latitud','longitud','descripcion','nivelPeligro']

