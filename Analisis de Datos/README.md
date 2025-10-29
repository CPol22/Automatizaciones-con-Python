# Lectura y Escritura de Archivos en Python

Este ejemplo muestra cómo **leer, escribir, guardar y modificar archivos de texto (`.txt`)** usando Python de forma segura y eficiente.

---

## Descripción

Python maneja nativamente la lectura y escritura de archivos mediante la función `open()` y el contexto `with`, que garantiza el cierre automático del archivo.

Modos de apertura más comunes:

| Modo | Acción | Descripción |
|------|--------|-------------|
| `'r'`  | Leer (read) | Abre el archivo solo para lectura. |
| `'w'`  | Escribir (write) | Sobrescribe el archivo si existe, o lo crea si no. |
| `'a'`  | Agregar (append) | Añade contenido al final sin borrar lo anterior. |
| `'r+'` | Leer y escribir | Permite ambas operaciones sin borrar contenido. |
| `'w+'` | Escribir y leer | Borra el contenido anterior y permite leer. |
| `'a+'` | Leer y agregar | Permite leer y escribir al final. |

---

```python
with open('ruta/del/archivo.txt', 'modo', encoding='utf-8') as archivo:
    # operaciones de lectura o escritura