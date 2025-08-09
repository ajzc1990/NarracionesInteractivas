import os
import cv2  # Para mostrar imágenes
import speech_recognition as sr

# Ruta del folder donde tienes las imágenes prediseñadas
imagenes_dir = 'imagenes/'
# Diccionario para relacionar palabras clave con imágenes
palabras_a_imagen = {
    'hamburguesa': 'hamburguesa.jpg',
    'perro': 'perro.png',
    'gato': 'gato.png'
}

def voz_a_texto():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo (esperando...):")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("No se detectó voz en el tiempo establecido.")
            return None
    try:
        texto = r.recognize_google(audio, language='es-ES')
        print("Texto detectado:", texto)
        return texto.lower()
    except:
        print("Error al reconocer.")
        return None

def mostrar_imagen(nombre_imagen):
    img_path = os.path.join(imagenes_dir, nombre_imagen)
    imagen = cv2.imread(img_path)
    cv2.imshow('Imagen relacionada', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Programamos relación
texto = voz_a_texto()
if texto:
    encontrado = False
    for palabra, imagen in palabras_a_imagen.items():
        if palabra in texto:
            print(f"Mostrando imagen de {palabra}")
            mostrar_imagen(imagen)
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ninguna palabra clave relacionada.")
else:
    print("No se pudo procesar el texto.")
