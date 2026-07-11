import json

print("🔍 Filtrando municipios de Antioquia...")

with open("assets/colombia_municipios.geojson", encoding="utf-8") as f:
    colombia = json.load(f)

antioquia = {
    "type": "FeatureCollection",
    "features": [
        f for f in colombia["features"]
        if f["properties"].get("DPTO_CCDGO") == "05"
    ]
}

print(f"✅ Municipios encontrados: {len(antioquia['features'])}")
print("\nLista de municipios:")
for f in antioquia["features"]:
    print(" →", f["properties"]["MPIO_CNMBR"])

with open("assets/antioquia.geojson", "w", encoding="utf-8") as f:
    json.dump(antioquia, f, ensure_ascii=False)

print("\n✅ Guardado como assets/antioquia.geojson")