from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  LoginView, UserView, LogoutView,incidenteCreate, callePeligrosaCreate, RegisterClienteView, callePeligrosaLista, comentarioList, incidenteLista, UserInfoView,incidentesAprobados
from .views import comentarioViewSet, likeViewSet, CambiarEstadoIncidente
router = DefaultRouter()
router.register(r'comentarios', comentarioViewSet, basename='comentario')
router.register(r'likes', likeViewSet, basename='like')

urlpatterns = [
    path('loginUser/', LoginView.as_view(), name='login_user'),
    path('users/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout_user'),
    path('incidente/', incidenteCreate.as_view(), name='incidente'),
    path('callePeligrosa/', callePeligrosaCreate.as_view(), name='calle peligrosa'),
    path('registerUser/', RegisterClienteView.as_view(), name='Register client'),
    path('callePeligrosaLista/', callePeligrosaLista.as_view(), name='Lista de calles peligrosas'),
    path('listcomentario/', comentarioList.as_view(), name='lista de comentarios'),
    path('userdIdInfo/', UserInfoView.as_view(), name='Info del user'),
    path('listaIncidente/',incidenteLista.as_view(), name='Lista incidentes' ),
    path('listaInciAprobado/',incidentesAprobados.as_view(), name='Lista incidentes aprobados' ),
    path('incidentes/<int:pk>/cambiar_estado/',CambiarEstadoIncidente.as_view(), name='cambiar estado' ),
    path('', include(router.urls)),
    
]
