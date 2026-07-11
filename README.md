# 🗺️ Nuestros Viajes por Antioquia

Un mapa interactivo y romántico para registrar los municipios de Antioquia que has visitado, con fotos de cada viaje.

🌐 **Demo en vivo:** [alexahurtado08.github.io/mapa-antioquia](https://alexahurtado08.github.io/mapa-antioquia)

---

## ✨ ¿Qué hace?

- Muestra el mapa real de Antioquia con los 125 municipios
- Los municipios visitados se colorean con colores pastel únicos
- Al hacer clic en un municipio aparece la foto del viaje
- Tooltip con el nombre del municipio al pasar el mouse
- Contador de municipios visitados

---

## 🛠️ Tecnologías usadas

- **Python** — para procesar el GeoJSON y registrar los viajes
- **D3.js** — para dibujar el mapa geográfico
- **HTML + CSS** — para la interfaz
- **GeoJSON** del DANE — datos oficiales de los municipios de Colombia

---

## 🚀 Cómo usar este proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/alexahurtado08/mapa-antioquia.git
cd mapa-antioquia
```

### 2. Instala Python

Necesitas Python 3 instalado. Puedes descargarlo en [python.org](https://python.org).

### 3. Descarga el mapa base

Corre este script una sola vez para descargar el GeoJSON de Colombia y generar el de Antioquia:

```bash
py preparar_mapa.py
```

Esto crea el archivo `assets/antioquia.geojson` que el mapa necesita.

---

## 📸 Cómo agregar tus fotos

### Paso 1 — Crea la carpeta de fotos

Dentro del proyecto crea la carpeta:

```
assets/
  fotos/     ← crea esta carpeta
```

### Paso 2 — Agrega tus fotos

Nombra cada foto con el nombre del municipio **en mayúsculas**, tal como aparece en esta lista:

| Nombre del archivo | Municipio |
|--------------------|-----------|
| `MEDELLÍN.jpg` | Medellín |
| `JERICÓ.jpg` | Jericó |
| `JARDÍN.jpg` | Jardín |
| `GUATAPÉ.jpg` | Guatapé |
| `PUEBLORRICO.jpg` | Pueblorrico |

> ⚠️ **Importante:** Los nombres deben incluir tildes y estar en mayúsculas exactamente como aparecen en el mapa. Puedes ver la lista completa de los 125 municipios corriendo `py explorar_municipios.py`.

Los formatos aceptados son `.jpg`, `.jpeg` y `.png`.

### Paso 3 — Registra tus viajes

Corre el script que escanea la carpeta y genera el archivo de datos:

```bash
py registrar_viajes.py
```

Verás algo así:

```
✅ JERICÓ → JERICÓ
✅ JARDÍN → JARDÍN
🗺️  Total municipios con foto: 2
✅ Guardado en assets/viajes.json
```

### Paso 4 — Abre el mapa

Abre `index.html` con la extensión **Live Server** de VS Code, o directamente en tu navegador. ¡Los municipios con foto aparecerán coloreados en el mapa!

---

## 🔄 Flujo para agregar nuevos viajes

Cada vez que regreses de un viaje:

1. Agrega la foto a `assets/fotos/` con el nombre del municipio
2. Corre `py registrar_viajes.py`
3. Sube los cambios a GitHub:

```bash
git add .
git commit -m "agrego viaje a Nombre del Municipio"
git push
```

En 1-2 minutos el mapa en línea se actualiza automáticamente.

---

## 📁 Estructura del proyecto

```
mapa-antioquia/
├── assets/
│   ├── fotos/              ← tus fotos van aquí (no se suben a GitHub)
│   ├── antioquia.geojson   ← mapa de municipios
│   └── viajes.json         ← generado automáticamente
├── index.html              ← el mapa
├── preparar_mapa.py        ← descarga y filtra el GeoJSON
├── registrar_viajes.py     ← escanea las fotos y genera viajes.json
├── explorar.py             ← utilidad para explorar el SVG
└── .gitignore
```

---

## 🗺️ Lista completa de municipios

<details>
<summary>Ver los 125 municipios de Antioquia</summary>

ABEJORRAL, ABRIAQUÍ, ALEJANDRÍA, AMAGÁ, AMALFI, ANDES, ANGELÓPOLIS, ANGOSTURA, ANORÍ, ANZÁ, APARTADÓ, ARBOLETES, ARGELIA, ARMENIA, BARBOSA, BELMIRA, BELLO, BETANIA, BETULIA, BRICEÑO, BURITICÁ, CÁCERES, CAICEDO, CALDAS, CAMPAMENTO, CAÑASGORDAS, CARACOLÍ, CARAMANTA, CAREPA, CAROLINA, EL CARMEN DE VIBORAL, CAUCASIA, CHIGORODÓ, CISNEROS, CIUDAD BOLÍVAR, COCORNÁ, CONCEPCIÓN, CONCORDIA, COPACABANA, DABEIBA, DONMATÍAS, EBÉJICO, EL BAGRE, ENTRERRÍOS, ENVIGADO, FREDONIA, FRONTINO, GIRALDO, GIRARDOTA, GÓMEZ PLATA, GRANADA, GUADALUPE, GUARNE, GUATAPÉ, HELICONIA, HISPANIA, ITUANGO, ITAGÜÍ, JARDÍN, JERICÓ, LA CEJA, LA ESTRELLA, LA PINTADA, LA UNIÓN, LIBORINA, MACEO, MARINILLA, MEDELLÍN, MONTEBELLO, MUTATÁ, NARIÑO, NECHÍ, NECOCLÍ, OLAYA, PEÑOL, PEQUE, PUEBLORRICO, PUERTO BERRÍO, PUERTO NARE, PUERTO TRIUNFO, REMEDIOS, RETIRO, RIONEGRO, SABANALARGA, SALGAR, SAN ANDRÉS DE CUERQUÍA, SAN CARLOS, SAN FRANCISCO, SAN JERÓNIMO, SAN JOSÉ DE LA MONTAÑA, SAN JUAN DE URABÁ, SAN LUIS, SAN PEDRO DE LOS MILAGROS, SAN PEDRO DE URABÁ, SAN RAFAEL, SAN ROQUE, SAN VICENTE FERRER, SANTA BÁRBARA, SANTA FÉ DE ANTIOQUIA, SANTA ROSA DE OSOS, SANTO DOMINGO, EL SANTUARIO, SEGOVIA, SOPETRÁN, SONSÓN, TÁMESIS, TARAZÁ, TARSO, TITIRIBÍ, TOLEDO, TURBO, URAMITA, URRAO, VALDIVIA, VALPARAÍSO, VEGACHÍ, VENECIA, VIGÍA DEL FUERTE, YALÍ, YARUMAL, YOLOMBÓ, YONDÓ, ZARAGOZA

</details>

---

## 💕 Créditos

Hecho con amor para registrar aventuras en pareja por el departamento de Antioquia, Colombia.

Datos geográficos: [DANE — Marco Geoestadístico Nacional 2018](https://geoportal.dane.gov.co/)
