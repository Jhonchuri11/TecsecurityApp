from rest_framework import serializers
from .models import User, Calle, Comentario, Incidentes, CallePeligrosas

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            'id','name','email','numero','password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class CalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calle
        fields = ['id','nombres','latitud','longitud','nivelSeguridad']

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['idCalle','comentario']

class IncidentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidentes
        fields = ['id','idusuario','latitud','longitud','descripcion','aprobado']

class CallesPeligrosaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallePeligrosas
        fields = ['id','nombre','latitud','longitud','descripcion','nivelPeligro']

