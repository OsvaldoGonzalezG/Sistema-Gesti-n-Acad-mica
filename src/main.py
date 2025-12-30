# Requisito: Uso de import para reutilizar funciones en diferentes archivos
import estudiantes
import validaciones

def mostrar_menu():
    """Muestra las opciones disponibles en la consola."""
    print("\n" + "="*30)
    print("  SISTEMA DE GESTIÓN ACADÉMICA")
    print("="*30)
    print("1. Registrar nuevo estudiante")
    print("2. Inscribir en una materia ")
    print("3. Cargar nota ")
    print("4. Calcular promedio ")
    print("5. Mostrar listado completo")
    print("6. Salir")
    print("="*30)

def ejecutar_sistema():
    """
    Función principal que implementa el bucle de iteración (while) 
    y condicionales (if, elif, else) para la toma de decisiones.
    """
    while True:
        # Menú de interfaz de usuario
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            # Captura de información y validación]
            id_est = validaciones.validar_entero("Ingrese ID único: ")
            nombre = validaciones.validar_texto("Ingrese nombre completo: ")
            edad = validaciones.validar_entero("Ingrese edad: ")
            estudiantes.registrar_estudiante(id_est, nombre, edad)

        elif opcion == "2":
            id_est = validaciones.validar_entero("ID del estudiante: ")
            materia = validaciones.validar_texto("Nombre de la materia: ")
            estudiantes.inscribir_materia(id_est, materia)

        elif opcion == "3":
            id_est = validaciones.validar_entero("ID del estudiante: ")
            nota = validaciones.validar_entero("Ingrese la calificación (0-10): ")
            estudiantes.agregar_nota(id_est, nota)

        elif opcion == "4":
            id_est = validaciones.validar_entero("ID del estudiante para promedio: ")
            promedio = estudiantes.calcular_promedio(id_est)
            if promedio is not None:
                # Formateo de salida
                print(f"\n✅ El promedio calculado es: {promedio:.2f}")
            else:
                print("\n❌ No se encontró al estudiante o no tiene notas.")

        elif opcion == "5":
            # Visualización de información
            estudiantes.mostrar_estudiantes()

        elif opcion == "6":
            # Guardamos los datos antes de salir
            estudiantes.guardar_datos_archivo()
            print("Cerrando sistema. ¡Éxito en tu proyecto!")
            break

        else:
            print("⚠️ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    ejecutar_sistema()
