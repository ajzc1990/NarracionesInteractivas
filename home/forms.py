from django import forms
from .models import Usuario, Localidad, Departamento, Provincia, Jardin, Sesion, Cuento, Sesion_Cuento, Pictograma, Palabra, Reporte_General

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class LocalidadForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = '__all__'

class JardinForm(forms.ModelForm):
    class Meta:
        model = Jardin
        fields = '__all__'

class SesionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = '__all__'

class CuentoForm(forms.ModelForm):
    class Meta:
        model = Cuento
        fields = '__all__'

class Sesion_CuentoForm(forms.ModelForm):
    class Meta:
        model = Sesion_Cuento
        fields = '__all__'

class PictogramaForm(forms.ModelForm):
    class Meta:
        model = Pictograma
        fields = '__all__'

class PalabraForm(forms.ModelForm):
    class Meta:
        model = Palabra
        fields = '__all__'

class ReporteGeneralForm(forms.ModelForm):
    class Meta:
        model = Reporte_General
        fields = '__all__'

from django import forms
from .models import Narracion

class NarracionForm(forms.ModelForm):
    class Meta:
        model = Narracion
        fields = ['archivo_audio']
        widgets = {
            'archivo_audio': forms.ClearableFileInput(attrs={'accept': 'audio/*'}),
        }
