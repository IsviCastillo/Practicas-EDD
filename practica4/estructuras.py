# Se usa deque en vez de list para la fila porque popleft() es O(1);
# con una lista normal, remover el primer elemento sería O(n).

# La bolsa se maneja como pila (LIFO) porque así funciona físicamente
# el despacho: lo último que se metió es lo primero que queda a la mano.

# Se usa set para membresías y cupones porque la verificación de
# pertenencia (in) es O(1) en promedio, ideal para validar unicidad
# sin recorrer toda la colección.

from collections import deque

# Fila de clientes - FIFO
fila_caja = deque()

# Membresías vigentes - SET
membresias = {
    "MEM 01",
    "MEM 02",
    "MEM 03"
}

# Cupones que ya fueron utilizados - SET
cupones_usados = set()

# Información de los clientes (ya cargada, sin pedir datos por teclado)
clientes = {
    "Ricardo": {
        "productos": ["Pan", "Leche", "Huevos"],
        "membresia": "MEM 01",
        "cupon": "Descuento del 10 %"
    },
    "Luis": {
        "productos": ["Arroz", "Frijoles"],
        "membresia": None,
        "cupon": "Descuento del 10 %"
    },
    "Rosalia": {
        "productos": ["Detergente", "Jabón", "Shampoo", "Toallas"],
        "membresia": "MEM 02",
        "cupon": None
    }
}

# Se agregan los clientes a la fila en el orden en que llegaron
fila_caja.append("Ricardo")
fila_caja.append("Luis")
fila_caja.append("Rosalia")


# FUNCION: VALIDAR MEMBRESIA

def validar_membresia(codigo):
    if codigo is None:
        print("El cliente no tiene membresía.")
        return False

    if codigo in membresias:
        print(f"Membresía válida: {codigo}")
        return True

    print(f"Membresía no válida: {codigo}")
    return False


# FUNCION: UTILIZAR CUPON

def usar_cupon(codigo):
    if codigo is None:
        print("El cliente no tiene cupón.")
        return False

    # Verificar si el cupón ya fue utilizado en esta sesión
    if codigo in cupones_usados:
        print(f"El cupón {codigo} ya fue utilizado.")
        return False

    cupones_usados.add(codigo)
    print(f"Cupón aplicado: {codigo}")
    return True


# FUNCION: PROCESAR PRODUCTOS (LIFO)

def procesar_productos(productos):
    print("--- DESPACHO DE PRODUCTOS ---")

    # Se usa una copia como pila para no modificar la lista original
    bolsa = productos.copy()

    if not bolsa:
        print("El cliente no tiene productos.")
        return

    print("Orden en que fueron guardados:", bolsa)
    print("Orden de registro/despacho:")

    while bolsa:
        producto = bolsa.pop()
        print(f"Registrando producto: {producto}")


# FUNCION: COBRAR CLIENTE (FIFO)


def cobrar_cliente():
    print("\n--- COBRAR CLIENTE ---")

    # Validar que haya alguien en la fila
    if not fila_caja:
        print("No hay clientes en la fila.")
        print("No se puede realizar el cobro.")
        return

    # Se atiende al primer cliente que llegó
    cliente = fila_caja.popleft()
    print(f"Atendiendo al cliente: {cliente}")

    informacion = clientes[cliente]

    validar_membresia(informacion["membresia"])
    usar_cupon(informacion["cupon"])
    procesar_productos(informacion["productos"])

    print(f"Compra de {cliente} procesada.")


# EJECUCIÓN DEL PROGRAMA

print("Fila inicial:", list(fila_caja))

# Se cobra a todos los clientes que están en la fila
while fila_caja:
    cobrar_cliente()

# Se intenta cobrar cuando ya no queda nadie en la fila
cobrar_cliente()