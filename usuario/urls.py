from django.conf.urls import url
from usuario.views import index, Iniciar_sesion,tablero_view,RegistrarUsuario

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^Usuario/Registrar/', RegistrarUsuario.as_view(), name="registrar"),
    url(r'^Usuario/Login/', Iniciar_sesion),
    url(r'^nuevo', tablero_view, name='tablero_view'),


]
