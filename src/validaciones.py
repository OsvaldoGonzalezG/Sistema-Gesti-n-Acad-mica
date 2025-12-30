def validar_entero(mensaje):
    """
    Valida que la entrada sea un número entero.
    Utiliza un bloque try-except para manejar errores de tipo ValueError.
    """
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            # Requisito: Validación de entradas para evitar errores en los datos
            print("Error: Por favor, ingrese un número válido.")

def validar_texto(mensaje):
    """
    Valida que el texto no esté vacío y elimina espacios innecesarios.
    Garantiza la integridad de la información ingresada.
    """
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error: El campo no puede estar vacío.")
