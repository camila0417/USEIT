from django.shortcuts import render , redirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from usuario.forms import TableroForm,RegistroForm 

# Create your views here.

class RegistrarUsuario(CreateView):
    model = User
    template_name = 'Registrar_Usuarios.html'
    form_class = RegistroForm
    sucess_url = reverse_lazy('usuario:index')

def index(request):
    return render(request, 'index.html')

def Registrar(request):
    return render(request, 'Registrar_Usuarios.html')

def Iniciar_sesion(request):
    return render(request, 'Logins_Usuarios.html')

def tablero_view(request):
	if request.method == 'POST':
		form = TableroForm (request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	else:
		form = TableroForm ()
	return render(request, 'Registrar_tablero.html', {'form':form})
