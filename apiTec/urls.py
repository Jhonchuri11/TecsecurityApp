from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, callesCreate, comentarioCreate, incidenteCreate, callePeligrosaCreate

urlpatterns = [
    path('registerUser/', RegisterView.as_view(), name='register_user'),
    path('loginUser/', LoginView.as_view(), name='login_user'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout_user'),
    path('calles/', callesCreate.as_view(), name='Creacion de calles seguras'),
    path('comentario/', comentarioCreate.as_view(), name='comentario'),
    path('incidente/', incidenteCreate.as_view(), name='incidente'),
    path('callePeligrosa/', callePeligrosaCreate.as_view(), name='calle peligrosa')
    
]
