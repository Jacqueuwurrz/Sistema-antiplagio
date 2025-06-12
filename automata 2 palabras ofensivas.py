def contiene_palabra_ofensiva(msg):
    palabras = ["tonto", "idiota", "estúpido", "imbécil"]
    return any(p in msg.lower() for p in palabras)

def contiene_enlace(msg):
    return "http://" in msg or "https://" in msg or "www." in msg

def contiene_codigo_malicioso(msg):
    return "<script>" in msg or "eval(" in msg

def caracteres_repetidos(msg):
    count = 1
    for i in range(1, len(msg)):
        if msg[i] == msg[i-1]:
            count += 1
            if count >= 4:
                return True
        else:
            count = 1
    return False

def analizar_mensaje(msg):
    if (contiene_palabra_ofensiva(msg) or
        contiene_enlace(msg) or
        contiene_codigo_malicioso(msg) or
        caracteres_repetidos(msg)):
        return "🚫 Mensaje bloqueado: contiene contenido prohibido"
    return "✅ Mensaje enviado correctamente"

# Pruebas
mensajes = [
    "Eres un idiota",
    "Visita http://maliciosa.com",
    "Normal message",
    "Mira esto!!!",
    "eval(alert('Hola'))"
]

for m in mensajes:
    print(f"Mensaje: {m}")
    print(analizar_mensaje(m))
    print("---")
