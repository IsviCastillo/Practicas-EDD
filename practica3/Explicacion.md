# Documentación y explicación — Caso 1: Gestión de tareas pendientes usando LIFO

## Estructura seleccionada

Para este caso se seleccionó la estructura **LIFO (Last In, First Out)**, que significa **"Último en entrar, primero en salir"**.

Se eligió esta estructura porque permite administrar las tareas pendientes de manera que la última tarea agregada sea la primera en realizarse.

En este ejemplo se utiliza una **lista de Python (`list`)** como una pila.

## ¿Por qué se eligió LIFO?

LIFO es adecuada para este caso porque podemos imaginar que las tareas se van colocando una encima de otra. La última tarea agregada queda en la parte superior de la pila y, por lo tanto, es la primera que se puede retirar.

Por ejemplo:

- Primero se agrega: `Hacer tarea de Python`
- Después: `Estudiar para el examen`
- Finalmente: `Realizar investigación`

Al utilizar LIFO, la primera tarea que se realiza será `Realizar investigación`, porque fue la última que se agregó.

## Métodos utilizados en `ActividadDeClase.py`

### `append()`

Se utilizó el método `append()` para **agregar tareas al final de la lista**, que en este caso representa la parte superior de la pila.

```python
materias.append("Hacer tarea de Python")
materias.append("Estudiar para el examen")
materias.append("Realizar investigación")
```

#### ¿Por qué se usa?

En una estructura LIFO, cada nueva tarea debe agregarse al final de la lista para que quede encima de las tareas anteriores. Esto permite que la última tarea agregada sea la primera en salir. Por eso `append()` es el método correcto para empujar elementos a la pila.

### `pop()`

Se usó `pop()` para **retirar el último elemento agregado** de la lista.

```python
while materias:
    print("Tarea realizada:", materias.pop())
```

#### ¿Por qué se usa?

`pop()` elimina el elemento que está en la parte superior de la pila. Como la estructura es LIFO, la tarea más reciente es la primera en retirarse. Esto refleja correctamente el comportamiento de una pila: último en entrar, primero en salir.

### `while materias:`

Este ciclo se usa para seguir ejecutándose **mientras la pila tenga elementos**.

```python
while materias:
    print("Tarea realizada:", materias.pop())
```

#### ¿Por qué se usa?

La idea del programa es procesar todas las tareas pendientes hasta que la lista quede vacía. El `while` verifica si la pila aún contiene elementos y, si es así, continúa sacando tareas. Cuando la pila está vacía, el ciclo termina de forma automática.

### `if materias:`

Se usa para comprobar si la lista todavía tiene tareas pendientes.

```python
if materias:
    print("Todavía hay tareas pendientes.")
else:
    print("La pila está vacía, no hay tareas por realizar.")
```

#### ¿Por qué se usa?

Después de ejecutar `pop()`, puede quedar la pila vacía. El `if` permite mostrar un mensaje según el estado final de la pila y confirma si aún quedan tareas por completar.

## Resumen

Los métodos y estructuras utilizadas en `ActividadDeClase.py` son adecuados porque:

- `append()` agrega nuevas tareas al final, como una pila.
- `pop()` elimina la más reciente, siguiendo la regla LIFO.
- `while` procesa cada tarea hasta que la pila queda vacía.
- `if` verifica si todavía hay tareas pendientes.

Esto hace que el ejemplo sea una representación clara y real de una pila en Python.