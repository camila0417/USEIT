from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from usuario.models import Tablero
from django import forms

class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
		}


class TableroForm(forms.ModelForm):

    class Meta:
        model = Tablero

        fields = [
            'nombre_tablero',
            'id_creador',
            'estado',
        ]
        labels = {
            'nombre_tablero': 'Nombre',
            'id_creador': 'Dueño',
            'estado':'Estado',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'id_creador': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxSelectMultiple(),
        }
