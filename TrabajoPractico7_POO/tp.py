#EJERCICIO1
""" class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Ejemplo de uso
rect = Rectangulo(4, 5)
print("Área del rectángulo:", rect.calcular_area())
 """

#EJERCICIO2
""" class Mate:
    def __init__(self, n):
        self.n = n
        self.cebadas_restantes = n
        self.estado = 'vacío'

    def cebar(self):
        if self.estado == 'lleno':
            raise Exception("¡Cuidado! ¡Te quemaste!")
        self.estado = 'lleno'

    def beber(self):
        if self.estado == 'vacío':
            raise Exception("¡El mate está vacío!")
        self.estado = 'vacío'
        if self.cebadas_restantes > 0:
            self.cebadas_restantes -= 1
        else:
            print("Advertencia: el mate está lavado.")

# Ejemplo de uso
mate = Mate(3)
mate.cebar()
mate.beber()
mate.cebar()
mate.beber()
mate.cebar()
mate.beber()
mate.cebar()
mate.beber() """

#EJERCICIO3
""" class Corcho:
    def __init__(self, bodega):
        self.bodega = bodega

class Botella:
    def __init__(self, corcho):
        self.corcho = corcho

class Sacacorchos:
    def __init__(self):
        self.corcho = None

    def destapar(self, botella):
        if botella.corcho is None:
            raise Exception("La botella ya está destapada.")
        if self.corcho is not None:
            raise Exception("El sacacorchos ya contiene un corcho.")
        self.corcho = botella.corcho
        botella.corcho = None

    def limpiar(self):
        if self.corcho is None:
            raise Exception("No hay corcho para limpiar.")
        self.corcho = None
 """

#EJERCICIO4
""" class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print(f"Restaurante: {self.restaurante_nombre}, Tipo: {self.tipo_comida}")

    def abrir_restaurante(self):
        print(f"{self.restaurante_nombre} está ahora abierto.")

class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)
        self.sabores = sabores

    def mostrar_sabores(self):
        print("Sabores disponibles:", ", ".join(self.sabores))

# Ejemplo
heladeria = Heladeria("Dulce Frío", "Helado", ["chocolate", "vainilla", "frutilla"])
heladeria.describir_restaurante()
heladeria.abrir_restaurante()
heladeria.mostrar_sabores()
 """

#EJERCICIO5
""" class Personaje:
    def __init__(self, vida, posicion, velocidad):
        self.vida = vida
        self.posicion = posicion  # puede ser un número o una tupla
        self.velocidad = velocidad

    def recibir_ataque(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            raise Exception("¡El personaje ha muerto!")

    def mover(self, direccion):
        self.posicion += self.velocidad * direccion

class Soldado(Personaje):
    def __init__(self, vida, posicion, velocidad, ataque):
        super().__init__(vida, posicion, velocidad)
        self.ataque = ataque

    def atacar(self, objetivo):
        objetivo.recibir_ataque(self.ataque)

class Campesino(Personaje):
    def __init__(self, vida, posicion, velocidad, cosecha):
        super().__init__(vida, posicion, velocidad)
        self.cosecha = cosecha

    def cosechar(self):
        return self.cosecha
 """

#EJERCICIO6
""" class Usuario:
    def __init__(self, nombre, apellido, email, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad

    def describir_usuario(self):
        print(f"Nombre: {self.nombre} {self.apellido}, Email: {self.email}, Edad: {self.edad}")

    def saludar_usuario(self):
        print(f"Hola, {self.nombre} {self.apellido}!")

# Ejemplo de uso
usuario1 = Usuario("Ana", "Pérez", "ana@gmail.com", 30)
usuario2 = Usuario("Luis", "Gómez", "luis@gmail.com", 25)

usuario1.describir_usuario()
usuario1.saludar_usuario()
usuario2.describir_usuario()
usuario2.saludar_usuario() """

#EJERCICIO7
""" class Admin(Usuario):
    def __init__(self, nombre, apellido, email, edad, privilegios):
        super().__init__(nombre, apellido, email, edad)
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print("Privilegios del administrador:")
        for p in self.privilegios:
            print(f"- {p}")

# Ejemplo
admin = Admin("Carla", "Sosa", "carla@admin.com", 40, [
    "puede postear en el foro",
    "puede borrar un post",
    "puede banear usuario"
])
admin.describir_usuario()
admin.mostrar_privilegios() """

#EJERCICIO8
""" class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print("Privilegios:")
        for p in self.privilegios:
            print(f"- {p}")

class Admin(Usuario):
    def __init__(self, nombre, apellido, email, edad, privilegios):
        super().__init__(nombre, apellido, email, edad)
        self.privilegios = Privilegios(privilegios)

# Ejemplo
admin = Admin("Mario", "Fernández", "mario@admin.com", 45, [
    "puede postear en el foro",
    "puede borrar un post",
    "puede banear usuario"
])
admin.privilegios.mostrar_privilegios()
 """