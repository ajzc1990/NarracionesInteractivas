from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Usuario, Localidad, Departamento, Provincia, Jardin, Sesion,Sesion_Cuento,Cuento,Pictograma,Palabra,Reporte_General
from .forms import UsuarioForm, LocalidadForm, DepartamentoForm, ProvinciaForm, JardinForm,SesionForm,Sesion_CuentoForm,CuentoForm,PictogramaForm,PalabraForm,ReporteGeneralForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import NarracionForm





def home(request):
    return render(request, 'inicio.html')
# Vistas para Usuario
class UsuarioListView(ListView):
    model = Usuario
    context_object_name = 'usuarios'
    template_name = 'lista_usuario.html'

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'nuevo_usuario.html'
    success_url = reverse_lazy('lista_usuarios')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'editar_usuario.html'
    success_url = reverse_lazy('lista_usuarios')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'borrar_usuario.html'
    success_url = reverse_lazy('lista_usuarios')

# Vistas para Localidad
class LocalidadListView(ListView):
    model = Localidad
    context_object_name = 'localidades'
    template_name = 'lista_localidad.html'

class LocalidadCreateView(CreateView):
    model = Localidad
    form_class = LocalidadForm
    template_name = 'nueva_localidad.html'
    success_url = reverse_lazy('lista_localidades')

class LocalidadUpdateView(UpdateView):
    model = Localidad
    form_class = LocalidadForm
    template_name = 'editar_localidad.html'
    success_url = reverse_lazy('lista_localidades')

class LocalidadDeleteView(DeleteView):
    model = Localidad
    template_name = 'borrar_localidad.html'
    success_url = reverse_lazy('lista_localidades')

# Vistas para Departamento
class DepartamentoListView(ListView):
    model = Departamento
    context_object_name = 'departamentos'
    template_name = 'lista_departamento.html'

class DepartamentoCreateView(CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'crear_departamento.html'
    success_url = reverse_lazy('lista_departamentos')
class DepartamentoUpdateView(UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'editar_departamento.html'
    success_url = reverse_lazy('lista_departamentos')

class DepartamentoDeleteView(DeleteView):
    model = Departamento
    template_name = 'borrar_departamento.html'
    success_url = reverse_lazy('lista_departamentos')

# Vistas para Provincia
class ProvinciaListView(ListView):
    model = Provincia
    context_object_name = 'provincias'
    template_name = 'lista_provincia.html'

class ProvinciaCreateView(CreateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'crear_provincia.html'
    success_url = reverse_lazy('lista_provincias')


class ProvinciaUpdateView(UpdateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'editar_provincia.html'
    success_url = reverse_lazy('lista_provincias')

class ProvinciaDeleteView(DeleteView):
    model = Provincia
    template_name = 'borrar_provincia.html'
    success_url = reverse_lazy('lista_provincias')



# Vistas para Jardín
class JardinListView(ListView):
    model = Jardin
    context_object_name = 'jardines'
    template_name = 'lista_jardin.html'

class JardinCreateView(CreateView):
    model = Jardin
    form_class = JardinForm
    template_name = 'nuevo_jardin.html'
    success_url = reverse_lazy('lista_jardines')

class JardinUpdateView(UpdateView):
    model = Jardin
    form_class = JardinForm
    template_name = 'editar_jardin.html'
    success_url = reverse_lazy('lista_jardines')

class JardinDeleteView(DeleteView):
    model = Jardin
    template_name = 'borrar_jardin.html'
    success_url = reverse_lazy('lista_jardines')


class SesionListView(ListView):
    model = Sesion
    context_object_name = 'sesiones'
    template_name = 'lista_sesion.html'

class SesionCreateView(CreateView):
    model = Sesion
    form_class = SesionForm
    template_name = 'nueva_sesion.html'
    success_url = reverse_lazy('lista_sesiones')

class SesionUpdateView(UpdateView):
    model = Sesion
    form_class = SesionForm
    template_name = 'editar_sesion.html'
    success_url = reverse_lazy('lista_sesiones')

class SesionDeleteView(DeleteView):
    model = Sesion
    template_name = 'borrar_sesion.html'
    success_url = reverse_lazy('lista_sesiones')

class Sesion_CuentoListView(ListView):
    model = Sesion_Cuento
    context_object_name = 'sesion_cuentos'
    template_name = 'lista_sesion_cuento.html'

class Sesion_CuentoCreateView(CreateView):
    model = Sesion_Cuento
    form_class = Sesion_CuentoForm
    template_name = 'nueva_sesion_cuento.html'
    success_url = reverse_lazy('lista_sesion_cuento')

class Sesion_CuentoUpdateView(UpdateView):
    model = Sesion_Cuento
    form_class = Sesion_CuentoForm
    template_name = 'editar_sesion_cuento.html'
    success_url = reverse_lazy('lista_sesion_cuento')

class Sesion_CuentoDeleteView(DeleteView):

    model = Sesion_Cuento
    template_name = 'borrar_sesion_cuento.html'
    success_url = reverse_lazy('lista_sesion_cuento')


class CuentoListView(ListView):
    model = Cuento
    context_object_name = 'cuentos'
    template_name = 'lista_cuento.html'

class CuentoCreateView(CreateView):
    model = Cuento
    form_class = CuentoForm
    template_name = 'nuevo_cuento.html'
    success_url = reverse_lazy('lista_cuento')

class CuentoUpdateView(UpdateView):
    model = Cuento
    form_class = CuentoForm
    template_name = 'editar_cuento.html'
    success_url = reverse_lazy('lista_cuento')

class CuentoDeleteView(DeleteView):
    model = Cuento
    template_name = 'borrar_cuento.html'
    success_url = reverse_lazy('lista_cuento')


class PictogramaListView(ListView):
    model = Pictograma
    context_object_name = 'pictogramas'
    template_name = 'lista_pictograma.html'

class PictogramaCreateView(CreateView):
    model = Pictograma
    form_class = PictogramaForm
    template_name = 'nuevo_pictograma.html'
    success_url = reverse_lazy('lista_pictograma')

class PictogramaUpdateView(UpdateView):
    model = Pictograma
    form_class = PictogramaForm
    template_name = 'editar_pictograma.html'
    success_url = reverse_lazy('lista_pictograma')

class PictogramaDeleteView(DeleteView):
    model = Pictograma
    template_name = 'borrar_pictograma.html'
    success_url = reverse_lazy('lista_pictograma')


class PalabraListView(ListView):
    model = Palabra
    context_object_name = 'palabras'
    template_name = 'lista_palabra.html'

class PalabraCreateView(CreateView):
    model = Palabra
    form_class = PalabraForm
    template_name = 'nueva_palabra.html'
    success_url = reverse_lazy('lista_palabra')

class PalabraUpdateView(UpdateView):
    model = Palabra
    form_class = PalabraForm
    template_name = 'editar_palabra.html'
    success_url = reverse_lazy('lista_palabra')

class PalabraDeleteView(DeleteView):
    model = Palabra
    template_name = 'borrar_palabra.html'
    success_url = reverse_lazy('lista_palabra')

class ReporteGeneralListView(ListView):
    model = Reporte_General
    context_object_name = 'reportes'
    template_name = 'lista_reporte_general.html'

class ReporteGeneralCreateView(CreateView):
    model = Reporte_General
    form_class = ReporteGeneralForm
    template_name = 'nuevo_reporte_general.html'
    success_url = reverse_lazy('lista_reporte_general')

class ReporteGeneralUpdateView(UpdateView):
    model = Reporte_General
    form_class = ReporteGeneralForm
    template_name = 'editar_reporte_general.html'
    success_url = reverse_lazy('lista_reporte_general')

class ReporteGeneralDeleteView(DeleteView):
    model = Reporte_General
    template_name = 'borrar_reporte_general.html'
    success_url = reverse_lazy('lista_reporte_general')


@login_required
def nueva_narracion(request, cuento_id):
    cuento = get_object_or_404(Cuento, pk=cuento_id)
    if request.method == 'POST':
        form = NarracionForm(request.POST, request.FILES)
        if form.is_valid():
            narracion = form.save(commit=False)
            narracion.usuario = request.user
            narracion.cuento = cuento
            narracion.save()
            # Aquí puedes agregar lógica para reproducir o gestionar la narración
            return redirect('detalle_cuento', pk=cuento.id)
    else:
        form = NarracionForm()
    return render(request, 'cuentos/nueva_narracion.html', {'form': form, 'cuento': cuento})