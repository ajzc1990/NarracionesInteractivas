import speech_recognition as sr
import openai
import requests
from PIL import Image
from io import BytesIO

# Configura tu API key de OpenAI
openai.api_key = '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'

# Función para captar voz y convertirla en texto
def voz_a_texto():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language='es-ES')  # cambia a 'en-US' si quieres en inglés
        print("Texto detectado:", texto)
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return None
    except sr.RequestError as e:
        print("Error con el servicio:", e)
        return None

# Función para generar la imagen con OpenAI
def texto_a_imagen(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url

# Función para descargar y mostrar la imagen
def mostrar_imagen(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

# Ejecutar todo en orden
texto = voz_a_texto()
if texto:
    url_imagen = texto_a_imagen(texto)
    mostrar_imagen(url_imagen)
else:
    print("No se puedo generar la imagen por el error en la voz.")
