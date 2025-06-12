import re

def validar_curp(curp):
    patron = r'^[A-Z]{4}\d{6}[HM][A-Z]{2}[A-Z]{3}[A-Z0-9]{2}\d$'
    if not re.match(patron, curp):
        return "Inválido: estructura incorrecta"
    return "Válido"

# Ejemplos
curps = [
    "GARC850101HMCLNS09",  # válida
    "JUEZ900231MDFRRL05",  # válida
    "abcd850101hmclns09",  # inválida por minúsculas
    "GARC850101XYCLNS09",  # sexo inválido
    "GARC850101HMCLN"      # incompleta
]

for c in curps:
    print(f"{c}: {validar_curp(c)}")
