# Manejo de Archivos .txt en Python

A continuación se muestra cómo **leer, escribir, guardar y modificar archivos de texto (`.txt`)** usando Python de forma segura y eficiente.

---

## Descripción

Python maneja nativamente la lectura y escritura de archivos mediante la función `open()` y el contexto `with`,  
que garantiza que el archivo se **abra correctamente** y se **cierre automáticamente** al finalizar, incluso si ocurre un error durante la ejecución.

Modos de apertura:

| Modo | Acción | Descripción |
|------|--------|-------------|
| `r`  | Leer (read) | Abre el archivo solo para lectura. |
| `w`  | Escribir (write) | Sobrescribe el archivo si existe, o lo crea si no. |
| `a`  | Agregar (append) | Añade contenido al final sin borrar lo anterior. |
| `r+` | Leer y escribir | Permite ambas operaciones sin borrar contenido. |
| `w+` | Escribir y leer | Borra el contenido anterior y permite leer. |
| `a+` | Leer y agregar | Permite leer y escribir al final. |

La sintaxis general es:

```python
with open('ruta/del/archivo.txt', 'modo', encoding='utf-8') as archivo:
```

## Operaciones Basicas:

### Lectura

| Método | Descripción | Ejemplo |
|------|--------|-------------|
| `read()`  | Lee todo el contenido del archivo como una sola cadena de texto. | contenido = archivo.read() |
| `readline()`  | Lee una sola línea por llamada. Ideal para bucles. | linea = archivo.readline() |
| `readlines()`  | Devuelve una lista con todas las líneas del archivo. | lineas = archivo.readlines() |

### Escritura

| Método | Descripción | Ejemplo |
|------|--------|-------------|
| `write(texto)` | Escribe una cadena de texto en el archivo. | archivo.write("Hola mundo\n") |
| `writelines(lista)` | Escribe una lista de cadenas línea por línea. | archivo.writelines(["Línea 1\n", "Línea 2\n"] |

## Manipulación de Texto

Python incluye un conjunto muy completo de métodos para **procesar, limpiar y transformar texto**,  
lo cual es fundamental cuando trabajas con archivos `.txt`, logs o datos no estructurados.

A continuación se resumen los **métodos más usados** con ejemplos prácticos.

---

###  Métodos de Limpieza de Texto

| Método | Descripción | Ejemplo | Resultado |
|---------|--------------|----------|------------|
| `strip()` | Elimina espacios, tabulaciones y saltos de línea al **inicio y final** de una cadena. | `"  Hola \n".strip()` | `'Hola'` |
| `lstrip()` | Elimina espacios o caracteres solo **a la izquierda**. | `"   texto".lstrip()` | `'texto'` |
| `rstrip()` | Elimina espacios o caracteres solo **a la derecha**. | `"texto   ".rstrip()` | `'texto'` |
| `replace(a,b)` | Reemplaza todas las ocurrencias de `a` por `b`. | `"Hola Mundo".replace("Mundo", "Python")` | `'Hola Python'` |
| `lower()` | Convierte todo el texto a **minúsculas**. | `"PYTHON".lower()` | `'python'` |
| `upper()` | Convierte todo el texto a **mayúsculas**. | `"python".upper()` | `'PYTHON'` |
| `capitalize()` | Pone **la primera letra en mayúscula**. | `"hola mundo".capitalize()` | `'Hola mundo'` |
| `title()` | Pone **en mayúscula cada palabra**. | `"hola mundo".title()` | `'Hola Mundo'` |
| `swapcase()` | Invierte mayúsculas/minúsculas. | `"PyThOn".swapcase()` | `'pYtHoN'` |

---

###  Métodos de Búsqueda y Conteo

| Método | Descripción | Ejemplo | Resultado |
|---------|--------------|----------|------------|
| `find(sub)` | Devuelve el índice donde aparece `sub` (o `-1` si no existe). | `"hola mundo".find("mundo")` | `5` |
| `rfind(sub)` | Igual que `find()`, pero busca desde el final. | `"hola hola".rfind("hola")` | `5` |
| `count(sub)` | Cuenta cuántas veces aparece una subcadena. | `"uno dos uno".count("uno")` | `2` |
| `startswith(sub)` | Devuelve `True` si la cadena **comienza** con `sub`. | `"Python".startswith("Py")` | `True` |
| `endswith(sub)` | Devuelve `True` si la cadena **termina** con `sub`. | `"script.py".endswith(".py")` | `True` |
| `in` | Evalúa si una subcadena está en otra cadena. | `"INFO" in "2025 INFO Servicio"` | `True` |

---

###  Métodos de División y Unión

| Método | Descripción | Ejemplo | Resultado |
|---------|--------------|----------|------------|
| `split(sep)` | Divide la cadena según un separador y devuelve una lista. | `"a,b,c".split(",")` | `['a', 'b', 'c']` |
| `rsplit(sep, n)` | Divide desde la derecha `n` veces. | `"1-2-3".rsplit("-", 1)` | `['1-2', '3']` |
| `splitlines()` | Divide una cadena por saltos de línea (`\n`). | `"uno\ndos\ntres".splitlines()` | `['uno', 'dos', 'tres']` |
| `'sep'.join(lista)` | Une una lista de cadenas usando `sep` como separador. | `', '.join(['uno', 'dos'])` | `'uno, dos'` |

**Ejemplo combinado:**
```python
texto = "  Hola, mundo, Python  "
palabras = texto.strip().split(",")
resultado = " | ".join(palabras)
print(resultado)  # 'Hola |  mundo |  Python'
```