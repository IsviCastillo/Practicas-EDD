# Practica 2: Estructuras de datos 
# Tema: Conjuntos (Set) vs Listas y Tuplas en Python

# Actividad: Crear un programa que demuestre el uso de listas, tuplas y sets en Python.

# Listas
lista_artistas = ["Shawn Mendes", "Dua Lipa", "The Weeknd", "Adele"]
print("Lista de artistas:", lista_artistas)
lista_artistas.remove("The Weeknd")  # Eliminar un artista de la lista
print("Lista de artistas actualizada:", lista_artistas)

# Se usa una lista porque permite agregar o eliminar artistas fácilmente.

# Tuplas
# Colección de entradas
coleccion_entrada = ("General", "VIP", "Premium", "Platino", "Diamante")
print("Colección de entradas :", coleccion_entrada)

# Se usa una tupla porque la colección de entradas es un conjunto de datos que no se modificará.

# Sets
# Registro de cursos aprobados
cursos_aprobados = {"Matemáticas", "Programación", "Servidores", "Física"}
print("Cursos aprobados:", cursos_aprobados)
cursos_aprobados.add("Sistemas Operativos")  # Agregar un curso aprobado
print("Cursos aprobados actualizados:", cursos_aprobados)

# Se usa un set porque los cursos aprobados no deben repetirse y se pueden agregar nuevos cursos aprobados.