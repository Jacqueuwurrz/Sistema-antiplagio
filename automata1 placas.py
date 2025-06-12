import re

def validar_placa(placa):
    patrones = {
        "ABC-1234": r"^[A-Z]{3}-\d{4}$",
        "123-ABC": r"^\d{3}-[A-Z]{3}$",
        "AB-12C": r"^[A-Z]{2}-\d{2}[A-Z]$"
    }
    for tipo, patron in patrones.items():
        if re.fullmatch(patron, placa):
            return f"Válida ({tipo})"
    return "Inválida"

# Pruebas
placas = ["ABC-1234", "123-ABC", "AB-12C", "A1B-2345", "12A-BC4", "XYZ-999", "1234-ABC"]
for p in placas:
    print(f"{p}: {validar_placa(p)}")
