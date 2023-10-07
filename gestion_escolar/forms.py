from django import forms
from .models import Docente, Estudiante

class DocenteForm(forms.ModelForm):
    SEXO_CHOICES = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    
    sexo = forms.ChoiceField(choices=SEXO_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Docente
        fields = ['nombres', 'apellidos', 'asignatura_id', 'fecha_de_nacimiento', 'sexo']

class EstudianteForm(forms.ModelForm):
    SEXO_CHOICES = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )

    sexo = forms.ChoiceField(choices=SEXO_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Estudiante
        fields = ['nombres', 'apellidos', 'fecha_nacimiento', 'sexo', 'telefono', 'direccion', 'documento', 'fecha_admision']
