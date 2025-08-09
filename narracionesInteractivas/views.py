# views.py
from django.shortcuts import render
from django.http import HttpResponse
import os
import speech_recognition as sr

# Ruta a las imágenes en tu proyecto
IMAGENES_DIR = os.path.join('static', 'imagenes')

# Diccionario de palabras clave y sus imágenes
PALABRAS_A_IMAGEN = {
    'hamburguesa': 'hamburguesa.jpg',
    'perro': 'perro.png',
    'gato': 'gato.png'
}

def reconocimiento(request):
    return render(request, 'reconocimiento.html')

def reconocimiento_voz(request):
    r = sr.Recognizer()
    
    # Usar la grabación desde micrófono
    with sr.Microphone() as source:
        try:
            # Ajuste de ruido y aceptación de entrada
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return HttpResponse("No se detectó voz en el tiempo establecido.")
    
    try:
        texto = r.recognize_google(audio, language='es-ES').lower()
    except sr.UnknownValueError:
        return HttpResponse("No se pudo entender el audio.")
    except sr.RequestError:
        return HttpResponse("Error en el servicio de reconocimiento de voz.")
    
    # Buscar palabras clave en el texto reconocido
    imagen_elegida = None
    for palabra, filename in PALABRAS_A_IMAGEN.items():
        if palabra in texto:
            imagen_elegida = filename
            break
    
    # Mostrar la imagen si se encontró alguna
    if imagen_elegida:
        return render(
            request,
            'mostrar_imagen.html',
            {
                'imagen_url': f'/static/imagenes/{imagen_elegida}',
                'texto': texto
            }
        )
    else:
        return HttpResponse("No se encontró ninguna palabra clave en el reconocimiento.")
