# Usando LIFO

materias = []  # Inicializar la pila

# Agregar tareas a la pila
materias.append("Hacer tarea de Python")
materias.append("Estudiar para el examen")
materias.append("Realizar investigación")

print("Pila actual:", materias)

# Sacar elementos de la pila utilizando LIFO
while materias:
    print("Tarea realizada:", materias.pop())

# Mostrar las tareas pendientes
print("Tareas pendientes:", materias)

# Comprobar si la pila está vacía
if materias:
    print("Todavía hay tareas pendientes.")
else:
    print("La pila está vacía, no hay tareas por realizar.")