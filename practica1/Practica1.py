# Diseña 5 tipos de datos cuyo valor deba validarse para poder existir
# No solo debe asignarse, debe cumplir una regla para ser válido


class Email:
    def __init__(self, direccion):
        # Evita aceptar una direccion que no tenga un "@" y un "."
        if "@" not in direccion or "." not in direccion:
            raise ValueError("Dirección de correo inválida")
        self.direccion = direccion


class Edad:
    def __init__(self, valor): 
        # Evita aceptar edades que no sean enteros o estén fuera de 0 a 120.
        if not isinstance(valor, int) or valor < 0 or valor > 120:
            raise ValueError("Edad fuera del rango permitido (0-120)")
        self.valor = valor


class Nota:
    def __init__(self, calificacion):
        # Evita aceptar notas menores que 0 o mayores que 10.
        if not (0.0 <= calificacion <= 10.0):
            raise ValueError("La nota debe estar entre 0.0 y 10.0")
        self.calificacion = calificacion


class Sexo:
    def __init__(self, sexo):
        # Evita aceptar valores diferentes de Hombre o Mujer.
        if sexo != "Hombre" and sexo != "Mujer":
            raise ValueError("Sexo debe ser Hombre o Mujer")
        self.sexo = sexo


class Activo:
    def __init__(self, activo):
        # Evita aceptar valores que no sean True o False.
        if not isinstance(activo, bool):
            raise ValueError("El valor debe ser True o False")
        self.activo = activo


# CASOS VÁLIDOS

try:
    e = Email("usuario@dominio.com")
    ed = Edad(20)
    n = Nota(8.5)
    s = Sexo("Hombre")
    a = Activo(True)

    print("Objetos creados exitosamente")

except ValueError as err:
    print("Error:", err)


# CASOS INVÁLIDOS


try:
    e_invalido = Email("correo_sin_arroba.com")
except ValueError as err:
    print("Email inválido:", err)


try:
    ed_invalida = Edad(-5)
except ValueError as err:
    print("Edad inválida:", err)


try:
    n_invalida = Nota(11.0)
except ValueError as err:
    print("Nota inválida:", err)


try:
    s_invalida = Sexo("Otro")
except ValueError as err:
    print("Sexo inválido:", err)


try:
    a_invalida = Activo("no es un booleano")
except ValueError as err:
    print("Activo inválido:", err)