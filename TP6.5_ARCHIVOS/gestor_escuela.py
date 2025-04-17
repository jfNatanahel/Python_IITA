import json
import os

ARCHIVO = "datos.json"

# ---------------------- PERSISTENCIA ----------------------
def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    else:
        return {"Alumnos": []}

def guardar_datos(datos):
    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)

# ---------------------- FUNCIONES ----------------------

def mostrar_todos(datos):
    if not datos["Alumnos"]:
        print("No hay alumnos registrados.")
        return
    for i, alumno in enumerate(datos["Alumnos"]):
        print(f"\nAlumno {i + 1}")
        for clave, valor in alumno.items():
            print(f"{clave}: {valor}")

def mostrar_un_alumno(datos):
    try:
        indice = int(input("Ingrese el número de alumno: ")) - 1
        alumno = datos["Alumnos"][indice]
        print(f"\nDatos del alumno {indice + 1}:")
        for clave, valor in alumno.items():
            print(f"{clave}: {valor}")
    except (IndexError, ValueError):
        print("Índice inválido.")

def agregar_alumno(datos):
    alumno = {
        "Nombre": input("Nombre: "),
        "Apellido": input("Apellido: "),
        "Fecha de nacimiento": input("Fecha de nacimiento (dd/mm/aaaa): "),
        "DNI": input("DNI: "),
        "Tutor": input("Nombre completo del tutor: "),
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }
    datos["Alumnos"].append(alumno)
    guardar_datos(datos)
    print("Alumno agregado correctamente.")

def modificar_alumno(datos):
    try:
        indice = int(input("Ingrese el número de alumno a modificar: ")) - 1
        alumno = datos["Alumnos"][indice]
        print("Campos disponibles para modificar:")
        campos = list(alumno.keys())
        for i, campo in enumerate(campos):
            print(f"{i + 1}. {campo}")
        opcion = int(input("Seleccione el campo a modificar: ")) - 1
        campo = campos[opcion]

        if campo == "Notas":
            nueva_nota = float(input("Ingrese una nueva nota: "))
            alumno["Notas"].append(nueva_nota)
        elif campo in ["Faltas", "Amonestaciones"]:
            nueva_cantidad = int(input(f"Ingrese nueva cantidad de {campo.lower()}: "))
            alumno[campo] = nueva_cantidad
        else:
            nuevo_valor = input(f"Ingrese nuevo valor para {campo}: ")
            alumno[campo] = nuevo_valor

        guardar_datos(datos)
        print("Datos actualizados correctamente.")
    except (IndexError, ValueError):
        print("Error: selección inválida.")

def expulsar_alumno(datos):
    try:
        indice = int(input("Ingrese el número de alumno a expulsar: ")) - 1
        alumno = datos["Alumnos"].pop(indice)
        guardar_datos(datos)
        print(f"Alumno {alumno['Nombre']} {alumno['Apellido']} expulsado correctamente.")
    except (IndexError, ValueError):
        print("Índice inválido.")

# ---------------------- MENÚ ----------------------

def menu():
    datos = cargar_datos()
    while True:
        print("\n----- MENÚ DE GESTIÓN ESCOLAR -----")
        print("1. Mostrar todos los alumnos")
        print("2. Mostrar un alumno específico")
        print("3. Agregar nuevo alumno")
        print("4. Modificar datos de alumno")
        print("5. Expulsar alumno")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_todos(datos)
        elif opcion == "2":
            mostrar_un_alumno(datos)
        elif opcion == "3":
            agregar_alumno(datos)
        elif opcion == "4":
            modificar_alumno(datos)
        elif opcion == "5":
            expulsar_alumno(datos)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# ---------------------- EJECUCIÓN ----------------------
if __name__ == "__main__":
    menu()
