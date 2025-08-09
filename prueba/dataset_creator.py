import os
import csv
import speech_recognition as sr
from PIL import Image, ImageDraw, ImageFont

# -- Configuración --
# Ruta donde guardarás las imágenes
dataset_dir = 'dataset/'
# Archivo CSV para las relaciones imagen-texto
csv_filename = 'dataset.csv'

# Crear directorio si no existe
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

# Función para capturar voz y convertir a texto
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

# Función para crear imagen con el texto
def crear_imagen_con_texto(texto, filename):
    img = Image.new('RGB', (800, 600), color='white')
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    # Dividir texto largo en líneas
    max_chars = 50
    lineas = []
    for i in range(0, len(texto), max_chars):
        lineas.append(texto[i:i+max_chars])
    y_text = 50
    for linea in lineas:
        d.text((50, y_text), linea, font=font, fill='black')
        y_text += 40

    path_imagen = os.path.join(dataset_dir, filename)
    img.save(path_imagen)
    img.show()
    return filename

# Lista de descripciones (puedes editarla)
descripciones = []

# Número de entradas
n = int(input("¿Cuántas narraciones quieres grabar? "))
for i in range(n):
    print(f"\n--- Entrada {i+1} ---")
    texto = voz_a_texto()
    if texto:
        filename = f'imagen_{i+1}.png'
        crear_imagen_con_texto(texto, filename)
        descripciones.append((filename, texto))
    else:
        print("Saltando esta entrada debido a error.")

# Crear archivo CSV
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['filename', 'caption'])
    for filename, caption in descripciones:
        writer.writerow([filename, caption])

print(f"\nDataset completado y guardado en {csv_filename}")
