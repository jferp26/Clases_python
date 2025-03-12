import json

import json

# Abre el archivo JSON en modo lectura
contactos = open("contactos.json","r")
datos= json.load(contactos)
contactos.close

# Muestra el contenido de los contactos
print(contactos)

# Abre el archivo JSON en modo lectura
with open("contactos.json", "r") as ct:
    contactos = json.load(ct)

# Muestra el contenido de los contactos
print(contactos)


