import re

def validar_comando(comando):
    patron_copiar = r'^copiar [a-z0-9]+\.[a-z]+$'
    patron_mover = r'^mover [a-z0-9]+\.[a-z]+ [a-z0-9]+\/$'
    patron_eliminar = r'^eliminar [a-z0-9]+\.[a-z]+$'

    if re.fullmatch(patron_copiar, comando):
        return "✅ Comando válido: copiar"
    elif re.fullmatch(patron_mover, comando):
        return "✅ Comando válido: mover"
    elif re.fullmatch(patron_eliminar, comando):
        return "✅ Comando válido: eliminar"
    else:
        return "❌ Comando inválido. Error de sintaxis o parámetro faltante."

# Simulación de terminal
while True:
    entrada = input("terminal> ")
    if entrada.strip().lower() == "salir":
        break
    print(validar_comando(entrada))
