
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

# === MODIFICAR O AGREGAR AL FINAL DE UN ARCHIVO EXISTENTE ===
nuevo_texto = "\n--- Análisis completado correctamente ---"

with open('datos/info_salida.txt', 'a', encoding='utf-8') as f:
    f.write(nuevo_texto)
