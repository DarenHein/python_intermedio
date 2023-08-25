import os

ruta_inicial = "/"  # Cambia esto a la ruta que quieras explorar

for root, dirs, files in os.walk(ruta_inicial):
    for directorio in dirs:
        print(os.path.join(root, directorio))
