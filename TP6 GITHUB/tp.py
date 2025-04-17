# Estructura inicial
Datos = {
    "Alumnos": []
}

# Función para mostrar los datos de todos los alumnos
def mostrar_todos():
    for i, alumno in enumerate(Datos["Alumnos"]):
        print(f"\nAlumno {i + 1}")
        for clave, valor in alumno.items():
            print(f"{clave}: {valor}")

# Función para mostrar un alumno específico por índice
def mostrar_alumno(indice):
    try:
        alumno = Datos["Alumnos"][indice]
        print(f"\nDatos del alumno {indice + 1}:")
        for clave, valor in alumno.items():
            print(f"{clave}: {valor}")
    except IndexError:
        print("Índice inválido.")

# Función para agregar un nuevo alumno
def agregar_alumno():
    nuevo = {
        "Nombre": input("Nombre: "),
        "Apellido": input("Apellido: "),
        "DNI": input("DNI: "),
        "Fecha de nacimiento": input("Fecha de nacimiento: "),
        "Tutor": input("Nombre del tutor: "),
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }
    Datos["Alumnos"].append(nuevo)
    print("Alumno agregado con éxito.")

# Función para modificar datos de un alumno
def modificar_alumno(indice):
    try:
        alumno = Datos["Alumnos"][indice]
        print("¿Qué campo deseas modificar?")
        for i, campo in enumerate(alumno.keys()):
            print(f"{i + 1}. {campo}")
        opcion = int(input("Número de opción: ")) - 1
        campos = list(alumno.keys())
        campo = campos[opcion]
        if campo == "Notas":
            nueva_nota = float(input("Ingrese una nueva nota: "))
            alumno["Notas"].append(nueva_nota)
        elif campo in ["Faltas", "Amonestaciones"]:
            alumno[campo] = int(input(f"Ingrese nueva cantidad de {campo.lower()}: "))
        else:
            alumno[campo] = input(f"Ingrese nuevo valor para {campo}: ")
        print("Datos actualizados.")
    except (IndexError, ValueError):
        print("Error: opción inválida.")

# Función para eliminar un alumno
def expulsar_alumno(indice):
    try:
        alumno = Datos["Alumnos"].pop(indice)
        print(f"Alumno {alumno['Nombre']} {alumno['Apellido']} expulsado.")
    except IndexError:
        print("Índice inválido.")

# Menú principal
def menu():
    while True:
        print("\n--- MENÚ ESCOLAR ---")
        print("1. Mostrar todos los alumnos")
        print("2. Ver datos de un alumno")
        print("3. Agregar nuevo alumno")
        print("4. Modificar datos de alumno")
        print("5. Expulsar alumno")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_todos()
        elif opcion == "2":
            indice = int(input("Ingrese el índice del alumno: ")) - 1
            mostrar_alumno(indice)
        elif opcion == "3":
            agregar_alumno()
        elif opcion == "4":
            indice = int(input("Ingrese el índice del alumno: ")) - 1
            modificar_alumno(indice)
        elif opcion == "5":
            indice = int(input("Ingrese el índice del alumno: ")) - 1
            expulsar_alumno(indice)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

# Ejecutar menú
menu()
