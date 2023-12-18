from rest_framework.views import APIView
from .serializers import ComentariosSerializer, IncidentesSerializer, CallesPeligrosaSerializer, ClienteSerializer, likeSerializer
from rest_framework.response import Response
from .models import  Comentario, Incidentes, CallePeligrosas, Cliente, Like
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework import generics, viewsets
from rest_framework.generics import CreateAPIView
import hashlib
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
        
    
# PUREBA DE REGISTRO CLIENTE

class RegisterClienteView(CreateAPIView):
    serializer_class = ClienteSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cliente_data = ClienteSerializer(response.data).data
        response.data = {"message": "Registro exitoso", "cliente_data": cliente_data}
        return response
    

# Login 
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        cliente = Cliente.objects.filter(email=email).first()

        if cliente is None:
            raise AuthenticationFailed('Usuario no funcional')
        
        if not self.verify_password(password, cliente.password):
            raise AuthenticationFailed('Contraseña incorrecta')
        
        payload = {
            'id': cliente.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        user_data = {
            'id': cliente.id,
            'nombre': cliente.nombre,
            'email': cliente.email,
            'numero': cliente.numero,
            'password': cliente.password
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'success': True,
            'data': {
                'cliente': user_data,
            },
            'jwt': token,
            'message': "Inicio de sesión exitoso"
        }
        return response
    
    def verify_password(self, raw_password, hashed_password):
        # Recoje el password y lo encripta  y lo compara con el hashed_password almacenado
        hashed_input_password = hashlib.sha256(raw_password.encode()).hexdigest()
        return hashed_input_password == hashed_password

class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Obtiene la información del usuario basándose en el token
        user = request.user
        serializer = ClienteSerializer(user)
        return Response(serializer.data)

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('No conectado!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('No conectado!')
        
        cliente = Cliente.objects.filter(id=payload['id']).first()
        serializer = ClienteSerializer(cliente)

        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data =  {
            'message': 'success' 
        }
        return response



class comentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk:None):
        comentario = self.get_object()
        cliente = request.user

        if not Like.objects.filter(cliente=cliente, comentario=comentario).exists():
            Like.objects.create(cliente=cliente, comentario=comentario)

        return Response({'status': 'success'})
    
    action_serializers = {
        'list': ComentariosSerializer,
        'retrieve': ComentariosSerializer,
        'create': ComentariosSerializer,
        'update': ComentariosSerializer,
        'partial_update': ComentariosSerializer,
        'destroy': ComentariosSerializer,
        'like': ComentariosSerializer, 
    }
    
class likeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = likeSerializer
    @action(detail=True, methods=['get'])
    def listas(self, request, *args, **kwargs):

        queryset = Like.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class comentarioList(generics.ListAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer


class incidenteCreate(generics.CreateAPIView):
    queryset = Incidentes.objects.all()
    serializer_class = IncidentesSerializer

class incidenteLista(generics.ListAPIView):
    queryset = Incidentes.objects.all()
    serializer_class = IncidentesSerializer

# Obteniendo solo los incidentes que hayan sido aprobados
class incidentesAprobados(generics.ListAPIView):
    queryset = Incidentes.objects.filter(estado='Aprobado')
    serializer_class = IncidentesSerializer

class CambiarEstadoIncidente(APIView):
    def put(self, request, pk):
        try:
            incidente = Incidentes.objects.get(pk=pk)
            nuevo_estado = request.data.get('estado', incidente.estado)
            incidente.estado = nuevo_estado
            incidente.save()
            return Response({'message': 'Estado actualizado correctamente'}, status=status.HTTP_200_OK)
        except Incidentes.DoesNotExist:
            return Response({'message': 'El incidente no existe'}, status=status.HTTP_404_NOT_FOUND)

class callePeligrosaCreate(generics.CreateAPIView):
    queryset = CallePeligrosas.objects.all()
    serializer_class = CallesPeligrosaSerializer
    
class callePeligrosaLista(generics.ListAPIView):
    queryset = CallePeligrosas.objects.all()
    serializer_class = CallesPeligrosaSerializer
