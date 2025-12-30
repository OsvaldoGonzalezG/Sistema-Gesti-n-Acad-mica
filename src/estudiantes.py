# Uso de listas (list) para almacenar conjuntos de datos
base_datos_estudiantes = []

def registrar_estudiante(id_estudiante, nombre, edad):
    """
    Registra un estudiante usando un diccionario (dict) para pares clave-valor.
    """
    # Implementación de diccionarios para gestionar información
    nuevo_estudiante = {
        "id": id_estudiante,
        "nombre": nombre,
        "edad": edad,
        "materias": set(),  # Uso de conjuntos (set) para evitar duplicados
        "notas": []         # Listas para manipular conjuntos de datos
    }
    base_datos_estudiantes.append(nuevo_estudiante)
    print(f"\n✅ Estudiante '{nombre}' registrado con éxito.")

def inscribir_materia(id_estudiante, materia):
    """
    Busca al estudiante por ID e intenta agregar una materia al set.
    """
    for estudiante in base_datos_estudiantes:
        if estudiante["id"] == id_estudiante:
            # Los conjuntos (set) no permiten duplicados automáticamente.
            estudiante["materias"].add(materia)
            print(f"✅ Materia '{materia}' asignada a {estudiante['nombre']}.")
            return
    print("❌ Error: No se encontró al estudiante.")

def agregar_nota(id_estudiante, nota):
    """
    Busca al estudiante por ID y agrega una nota a su lista de notas.
    """
    for est in base_datos_estudiantes:
        if est["id"] == id_estudiante:
            est["notas"].append(nota)
            print(f"✅ Nota {nota} agregada a {est['nombre']}.")
            return
    print("❌ Estudiante no encontrado.")

def sumar_notas_recursiva(notas, n):
    """
    Requisito: Implementación de funciones recursivas para cálculos específicos.
    Suma las notas de manera recursiva hasta llegar al caso base (n=0).
    """
    if n == 0:
        return 0
    else:
        return notas[n - 1] + sumar_notas_recursiva(notas, n - 1)

def calcular_promedio(id_estudiante):
    """
    Busca al estudiante y calcula su promedio utilizando la función recursiva.
    """
    for est in base_datos_estudiantes:
        if est["id"] == id_estudiante:
            if not est["notas"]:
                return 0
            total_notas = len(est["notas"])
            suma_total = sumar_notas_recursiva(est["notas"], total_notas)
            return suma_total / total_notas
    return None

def mostrar_estudiantes():
    """
    Muestra el listado de estudiantes registrados.
    """
    if not base_datos_estudiantes:
        print("\nNo hay estudiantes registrados.")
        return

    print("\n--- Listado de Estudiantes ---")
    for est in base_datos_estudiantes:
        materias = ", ".join(est["materias"]) if est["materias"] else "Ninguna"
        print(f"ID: {est['id']} | Nombre: {est['nombre']} | Materias: {materias}")

def guardar_datos_archivo(nombre_archivo="datos_estudiantes.txt"):
    """
    Requisito: Manejo de archivos (.txt) para persistencia de datos.
    Genera un reporte formateado con la información de salida.
    """
    if not base_datos_estudiantes:
        return
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("--- REPORTE DE GESTIÓN ACADÉMICA ---\n")
            archivo.write(f"{'ID':<10} | {'Nombre':<20} | {'Promedio':<10} | {'Materias'}\n")
            archivo.write("-" * 60 + "\n")
            for est in base_datos_estudiantes:
                materias = ", ".join(est["materias"]) if est["materias"] else "Ninguna"
                promedio = calcular_promedio(est["id"])
                prom_formateado = f"{promedio:.2f}" if promedio is not None else "0.00"
                archivo.write(f"{est['id']:<10} | {est['nombre']:<20} | {prom_formateado:<10} | {materias}\n")
        print(f"\n✅ Archivo '{nombre_archivo}' generado correctamente.")
    except Exception as e:
        print(f"Error al guardar: {e}")
