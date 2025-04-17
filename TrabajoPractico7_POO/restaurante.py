class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print(f"Restaurante: {self.restaurante_nombre}, Tipo: {self.tipo_comida}")

    def abrir_restaurante(self):
        print(f"{self.restaurante_nombre} está ahora abierto.")
