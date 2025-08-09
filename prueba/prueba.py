import speech_recognition as sr

# Crear un recognizer
r = sr.Recognizer()

# Usar el micrófono como fuente de audio
with sr.Microphone() as source:
    print("Di algo:")
    audio = r.listen(source)

# Intentar reconocer lo que se dijo
try:
    texto = r.recognize_google(audio, language='es-ES')  # Puedes cambiar a 'en-US' u otro
    print("Has dicho: " + texto)
except sr.UnknownValueError:
    print("No se pudo entender el audio")
except sr.RequestError as e:
    print("Error en la solicitud; {0}".format(e))
