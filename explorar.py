import xml.etree.ElementTree as ET

# Cargamos el SVG
tree = ET.parse("assets/antioquia.svg")
root = tree.getroot()

# Namespace del SVG (necesario para leerlo bien)
ns = {"svg": "http://www.w3.org/2000/svg"}

# Buscamos todos los <path> y mostramos su id y si tiene título
paths = root.findall(".//{http://www.w3.org/2000/svg}path")

print(f"Total de paths encontrados: {len(paths)}\n")

for path in paths[:10]:  # Mostramos los primeros 10
    path_id = path.get("id", "sin-id")
    title = path.find("{http://www.w3.org/2000/svg}title")
    label = title.text if title is not None else "sin nombre"
    print(f"ID: {path_id} | Nombre: {label}")