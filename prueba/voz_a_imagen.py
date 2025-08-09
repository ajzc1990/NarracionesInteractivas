import speech_recognition as sr
from PIL import Image, ImageDraw, ImageFont

# Función para convertir voz en texto
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
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return None
    except sr.RequestError as e:
        print("Error con el servicio:", e)
        return None

# Función para crear una imagen con texto
def crear_imagen_con_texto(texto):
    # Crear una imagen en blanco
    img = Image.new('RGB', (800, 600), color='white')
    d = ImageDraw.Draw(img)
    
    # Puedes usar una fuente predeterminada
    font = ImageFont.load_default()

    # Dividir el texto en varias líneas si es muy largo
    lineas = []
    max_chars = 40
    for i in range(0, len(texto), max_chars):
        lineas.append(texto[i:i+max_chars])
    y_text = 50
    for linea in lineas:
        d.text((50, y_text), linea, font=font, fill='black')
        y_text += 40

    # Guardar y mostrar la imagen
    img.save('texto_en_imagen.png')
    img.show()

# Programa principal
texto = voz_a_texto()
if texto:
    crear_imagen_con_texto(texto)
else:
    print("No se pudo crear la imagen.")
