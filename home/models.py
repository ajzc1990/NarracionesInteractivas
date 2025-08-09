from django.db import models
from django.contrib.auth.models import User 

class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    cp = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    # relacion con Departamento
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE, related_name='localidades')
    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    # relacion con Provincia
    provincia = models.ForeignKey('Provincia', on_delete=models.CASCADE, related_name='departamentos')
    def __str__(self):
        return self.nombre
class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    def __str__(self):
        return self.nombre

class Jardin(models.Model):
    id_jardin = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    cuil = models.CharField(max_length=45)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=8)
    apellido = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=15)
    tipo = models.CharField(max_length=45)
    jardìn = models.ForeignKey(Jardin, on_delete=models.CASCADE, null=True, blank=True)
    edad = models.CharField(max_length=45)

class Sesion(models.Model):
    id_sesion_usuario = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    localida = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    jardin = models.ForeignKey(Jardin, on_delete=models.CASCADE)
    hora = models.TimeField()
    fecha = models.DateField()
    def __str__(self):
        return f'Sesion {self.id_sesion_usuario} - {self.usuario}'

class Cuento(models.Model):
    id_cuento = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=45)
    version = models.CharField(max_length=45)
    texto = models.TextField()
    cantidad_palabras = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    # archivo_texto = models.FileField(upload_to='cuentos/textos/')  # Opcional, si quieres subir los textos
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo

class Sesion_Cuento(models.Model):
    id_sesion_cuento = models.AutoField(primary_key=True)
    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE)
    cuento = models.ForeignKey(Cuento, on_delete=models.CASCADE)
    tiempo_lectura = models.CharField(max_length=45)
    def __str__(self):
        return f'Sesion {self.sesion.id_sesion_usuario} - Cuento {self.cuento.titulo}'

class Pictograma(models.Model):
    id_pictograma = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    tamaño = models.CharField(max_length=45)
    cuento = models.ForeignKey(Cuento,related_name='pictogramas', on_delete=models.CASCADE)
    palabra = models.ForeignKey('Palabra', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='pictogramas/')
    def __str__(self):
        return self.palabra

class Palabra(models.Model):
    id_palabra = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)
    onda_voz = models.CharField(max_length=45)
    resultado_esperado = models.CharField(max_length=45)

class Narracion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cuento = models.ForeignKey(Cuento, on_delete=models.CASCADE)
    archivo_audio = models.FileField(upload_to='narraciones/audio/')
    fecha_grabacion = models.DateTimeField(auto_now_add=True)
    
    # Estado para controlar si se repite la narración
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('completa', 'Completa'), ('rechazada', 'Rechazada')], default='pendiente')

    def __str__(self):
        return f"{self.usuario.username} - {self.cuento.titulo} - {self.fecha_grabacion}"


class Reporte_General(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    sesion_cuento = models.ForeignKey(Sesion_Cuento, on_delete=models.CASCADE)



