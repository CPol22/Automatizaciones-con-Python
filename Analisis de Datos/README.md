# Manejo de Archivos .txt en Python

A continuación se muestra cómo **leer, escribir, guardar y modificar archivos de texto (`.txt`)** usando Python de forma segura y eficiente.

---

## Descripción

Python maneja nativamente la lectura y escritura de archivos mediante la función `open()` y el contexto `with`,  
que garantiza que el archivo se **abra correctamente** y se **cierre automáticamente** al finalizar, incluso si ocurre un error durante la ejecución.

Modos de apertura:

| Modo | Acción | Descripción |
|------|--------|-------------|
| `'r'`  | Leer (read) | Abre el archivo solo para lectura. |
| `'w'`  | Escribir (write) | Sobrescribe el archivo si existe, o lo crea si no. |
| `'a'`  | Agregar (append) | Añade contenido al final sin borrar lo anterior. |
| `'r+'` | Leer y escribir | Permite ambas operaciones sin borrar contenido. |
| `'w+'` | Escribir y leer | Borra el contenido anterior y permite leer. |
| `'a+'` | Leer y agregar | Permite leer y escribir al final. |

La sintaxis general es:

```python
with open('ruta/del/archivo.txt', 'modo', encoding='utf-8') as archivo:
    # operaciones de lectura o escritura
```
## Operaciones Basicas:



| Método | Descripción | Ejemplo |
|------|--------|-------------|
| `read()`  | Lee todo el contenido del archivo como una sola cadena de texto. | contenido = archivo.read() |
| `'readline()'`  | Lee una sola línea por llamada. Ideal para bucles. | linea = archivo.readline() |
| `'readlines()'`  | Devuelve una lista con todas las líneas del archivo. | lineas = archivo.readlines() |
| `'write(texto)'` | Leer y escribir | Permite ambas operaciones sin borrar contenido. |
| `'writelines(lista)'` | Escribir y leer | Borra el contenido anterior y permite leer. |
| `'a+'` | Leer y agregar | Permite leer y escribir al final. |