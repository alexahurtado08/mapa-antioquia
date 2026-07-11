import json
import os

# Lista de municipios en el GeoJSON (nombres exactos)
municipios_geojson = {

    # Agrega más correcciones aquí si las necesitas
}

carpeta_fotos = "assets/fotos"
viajes = {}

for archivo in os.listdir(carpeta_fotos):
    if archivo.lower().endswith((".jpg", ".jpeg", ".png")):
        nombre_sin_ext = os.path.splitext(archivo)[0].upper()
        
        # Corregimos el nombre si está en el diccionario
        nombre_correcto = municipios_geojson.get(nombre_sin_ext, nombre_sin_ext)
        
        viajes[nombre_correcto] = f"assets/fotos/{archivo}"
        print(f"✅ {nombre_sin_ext} → {nombre_correcto}")

# Guardamos el resultado
with open("assets/viajes.json", "w", encoding="utf-8") as f:
    json.dump(viajes, f, ensure_ascii=False, indent=2)

print(f"\n🗺️  Total municipios con foto: {len(viajes)}")
print("✅ Guardado en assets/viajes.json")