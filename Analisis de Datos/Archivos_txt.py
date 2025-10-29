'''
Python maneja nativamente la lectura y escritura de diferentes tipos de archivos, 
entre ellos los archivos de texto (.txt).

El comando general para trabajar con archivos es:
    with open('ruta/del/archivo.txt', 'modo', encoding='utf-8') as variable:

El parámetro 'modo' indica la acción que realizaremos:
    'r'  → leer (read)
    'w'  → escribir (write) → sobrescribe si ya existe
    'a'  → agregar (append) → escribe al final sin borrar el contenido
    'r+' → leer y escribir
    'w+' → escribir y leer (borra el contenido anterior)
    'a+' → leer y agregar al final del archivo

El bloque "with" garantiza que el archivo se cierre automáticamente al terminar.
'''

# === LECTURA DE ARCHIVO ===
with open('datos/texto.txt', 'r', encoding='utf-8') as f:
    # Lee todas las líneas y las guarda en una lista
    lineas = f.readlines()

info = []
error = []

# Recorremos línea por línea para separar las que contienen INFO y ERROR
for linea in lineas:
    if 'INFO' in linea:
        info.append(linea.strip())   # strip() elimina saltos de línea
    elif 'ERROR' in linea:
        error.append(linea.strip())

# Imprimimos las listas clasificadas
print("=== INFO ===")
print('\n'.join(info))

print("\n=== ERROR ===")
print('\n'.join(error))

# === ESCRITURA / GUARDADO EN NUEVOS ARCHIVOS ===

# Guardar las líneas INFO en un nuevo archivo
with open('datos/info_salida.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(info))

# Guardar las líneas ERROR en otro archivo
with open('datos/error_salida.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(error))

'''
Con esto:
- "info_salida.txt" contendrá todas las líneas con INFO
- "error_salida.txt" contendrá todas las líneas con ERROR
- Si los archivos no existen, Python los crea automáticamente
- Si ya existen, se sobrescriben (porque usamos modo 'w')
'''

# === MODIFICAR O AGREGAR AL FINAL DE UN ARCHIVO EXISTENTE ===
nuevo_texto = "\n--- Análisis completado correctamente ---"

with open('datos/info_salida.txt', 'a', encoding='utf-8') as f:
    f.write(nuevo_texto)

'''
Modo 'a' (append) agrega texto al final del archivo sin borrar el contenido anterior.
'''