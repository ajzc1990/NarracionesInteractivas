from django.urls import path
from . import views
from .views import ProvinciaUpdateView, ProvinciaDeleteView,DepartamentoUpdateView,DepartamentoDeleteView,LocalidadUpdateView,LocalidadDeleteView,UsuarioUpdateView,UsuarioDeleteView,JardinUpdateView,JardinDeleteView
from .views import (
    SesionListView, SesionCreateView,
    SesionUpdateView, SesionDeleteView
)
from .views import (
    Sesion_CuentoListView, Sesion_CuentoCreateView,
    Sesion_CuentoUpdateView, Sesion_CuentoDeleteView
)
from .views import (
    CuentoListView, CuentoCreateView,
    CuentoUpdateView, CuentoDeleteView
)
from .views import (
    PictogramaListView, PictogramaCreateView,
    PictogramaUpdateView, PictogramaDeleteView
)
from .views import (
    PalabraListView, PalabraCreateView,
    PalabraUpdateView, PalabraDeleteView
)
from .views import (
    ReporteGeneralListView, ReporteGeneralCreateView,
    ReporteGeneralUpdateView, ReporteGeneralDeleteView
)


urlpatterns = [
    path('', views.home, name='inicio'),
    # Ejemplo: vista para crear un nuevo usuario
    path('usuarios/', views.UsuarioListView.as_view(), name='lista_usuarios'),
    path('usuarios/nuevo/', views.UsuarioCreateView.as_view(), name='nuevo_usuario'),
    path('usuarios/editar/<int:pk>/', UsuarioUpdateView.as_view(), name='editar_usuario'),
    path('usuarios/borrar/<int:pk>/', UsuarioDeleteView.as_view(), name='borrar_usuario'),

    
    # Puedes agregar rutas similares para otros modelos
    path('localidades/', views.LocalidadListView.as_view(), name='lista_localidades'),
    path('localidades/nueva/', views.LocalidadCreateView.as_view(), name='nueva_localidad'),
    path('localidades/editar/<int:pk>/', LocalidadUpdateView.as_view(), name='editar_localidad'),
    path('localidades/borrar/<int:pk>/', LocalidadDeleteView.as_view(), name='borrar_localidad'),
    
    path('departamentos/', views.DepartamentoListView.as_view(), name='lista_departamentos'),
    path('departamentos/nuevo/', views.DepartamentoCreateView.as_view(), name='crear_departamento'),
    path('departamentos/editar/<int:pk>/', DepartamentoUpdateView.as_view(), name='editar_departamento'),
    path('departamentos/borrar/<int:pk>/', DepartamentoDeleteView.as_view(), name='borrar_departamento'),
    
    path('provincias/', views.ProvinciaListView.as_view(), name='lista_provincias'),
    path('provincias/nueva/', views.ProvinciaCreateView.as_view(), name='crear_provincia'),
    path('provincias/editar/<int:pk>/', ProvinciaUpdateView.as_view(), name='editar_provincia'),
    path('provincias/borrar/<int:pk>/', ProvinciaDeleteView.as_view(), name='borrar_provincia'),
    
    path('jardines/', views.JardinListView.as_view(), name='lista_jardines'),
    path('jardines/nuevo/', views.JardinCreateView.as_view(), name='nuevo_jardin'),
    path('jardines/editar/<int:pk>/', JardinUpdateView.as_view(), name='editar_jardin'),
    path('jardines/borrar/<int:pk>/', JardinDeleteView.as_view(), name='borrar_jardin'),

    # Añade más rutas para otros modelos según sea necesario
    path('sesiones/', SesionListView.as_view(), name='lista_sesiones'),
    path('sesiones/nueva/', SesionCreateView.as_view(), name='nueva_sesion'),
    path('sesiones/editar/<int:pk>/', SesionUpdateView.as_view(), name='editar_sesion'),
    path('sesiones/borrar/<int:pk>/', SesionDeleteView.as_view(), name='borrar_sesion'),

    path('sesion-cuentos/', Sesion_CuentoListView.as_view(), name='lista_sesion_cuento'),
    path('sesion-cuentos/nueva/', Sesion_CuentoCreateView.as_view(), name='nueva_sesion_cuento'),
    path('sesion-cuentos/editar/<int:pk>/', Sesion_CuentoUpdateView.as_view(), name='editar_sesion_cuento'),
    path('sesion-cuentos/borrar/<int:pk>/', Sesion_CuentoDeleteView.as_view(), name='borrar_sesion_cuento'),

    path('cuentos/', CuentoListView.as_view(), name='lista_cuento'),
    path('cuentos/nuevo/', CuentoCreateView.as_view(), name='nuevo_cuento'),
    path('cuentos/editar/<int:pk>/', CuentoUpdateView.as_view(), name='editar_cuento'),
    path('cuentos/borrar/<int:pk>/', CuentoDeleteView.as_view(), name='borrar_cuento'),

    path('pictogramas/', PictogramaListView.as_view(), name='lista_pictograma'),
    path('pictogramas/nuevo/', PictogramaCreateView.as_view(), name='nuevo_pictograma'),
    path('pictogramas/editar/<int:pk>/', PictogramaUpdateView.as_view(), name='editar_pictograma'),
    path('pictogramas/borrar/<int:pk>/', PictogramaDeleteView.as_view(), name='borrar_pictograma'),

    path('palabras/', PalabraListView.as_view(), name='lista_palabra'),
    path('palabras/nueva/', PalabraCreateView.as_view(), name='nueva_palabra'),
    path('palabras/editar/<int:pk>/', PalabraUpdateView.as_view(), name='editar_palabra'),
    path('palabras/borrar/<int:pk>/', PalabraDeleteView.as_view(), name='borrar_palabra'),

    path('reportes/', ReporteGeneralListView.as_view(), name='lista_reporte_general'),
    path('reportes/nuevo/', ReporteGeneralCreateView.as_view(), name='nuevo_reporte_general'),
    path('reportes/editar/<int:pk>/', ReporteGeneralUpdateView.as_view(), name='editar_reporte_general'),
    path('reportes/borrar/<int:pk>/', ReporteGeneralDeleteView.as_view(), name='borrar_reporte_general'),

    path('nueva_narracion/<int:cuento_id>/', views.nueva_narracion, name='nueva_narracion'),


    
]
