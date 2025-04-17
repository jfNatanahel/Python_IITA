# 1. Lista de todos los enteros entre 2 números (inclusive)
def lista_enteros(a, b):
    lista = []
    if a <= b:
        i = a
        while i <= b:
            lista += [i]
            i += 1
    else:
        i = b
        while i <= a:
            lista += [i]
            i += 1
    return lista


# 2. Lista de pares entre dos números (excluyendo los extremos)
def lista_pares_exclusivos(a, b):
    lista = []
    i = a + 1
    while i < b:
        if i % 2 == 0:
            lista += [i]
        i += 1
    return lista


# 3. Contar cuántas veces aparece un carácter en una cadena
def contar_caracter(cadena, caracter):
    contador = 0
    for c in cadena:
        if c.lower() == caracter.lower():
            contador += 1
    return contador


# 4. Lista de números primos entre dos números
def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def primos_entre(a, b):
    lista = []
    i = a
    while i <= b:
        if es_primo(i):
            lista += [i]
        i += 1
    return lista


# 5. Verificar si todos los números de una lista son pares
def todos_pares(lista):
    for numero in lista:
        if numero % 2 != 0:
            return False
    return True


# 6. Verificar si todos los números de una lista son primos
def todos_primos(lista):
    for numero in lista:
        if not es_primo(numero):
            return False
    return True
