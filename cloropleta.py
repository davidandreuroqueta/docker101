import geopandas as gpd
import matplotlib.pyplot as plt

datos = {
  "datos": [
    {
      "densidad_poblacion": 380.5,
      "id": "0",
      "pais_codigo": "BE",
      "pais_nombre": "Belgium"
    },
    {
      "densidad_poblacion": 62.5,
      "id": "1",
      "pais_codigo": "BG",
      "pais_nombre": "Bulgaria"
    },
    {
      "densidad_poblacion": 136.1,
      "id": "2",
      "pais_codigo": "CZ",
      "pais_nombre": "Czechia"
    },
    {
      "densidad_poblacion": 139.5,
      "id": "3",
      "pais_codigo": "DK",
      "pais_nombre": "Denmark"
    },
    {
      "densidad_poblacion": 235.5,
      "id": "4",
      "pais_codigo": "DE",
      "pais_nombre": "Germany"
    },
    {
      "densidad_poblacion": 30.9,
      "id": "5",
      "pais_codigo": "EE",
      "pais_nombre": "Estonia"
    },
    {
      "densidad_poblacion": 73.3,
      "id": "6",
      "pais_codigo": "IE",
      "pais_nombre": "Ireland"
    },
    {
      "densidad_poblacion": 81.3,
      "id": "7",
      "pais_codigo": "EL",
      "pais_nombre": "Greece"
    },
    {
      "densidad_poblacion": 94.3,
      "id": "8",
      "pais_codigo": "ES",
      "pais_nombre": "Spain"
    },
    {
      "densidad_poblacion": 106.9,
      "id": "9",
      "pais_codigo": "FR",
      "pais_nombre": "France"
    },
    {
      "densidad_poblacion": 70.7,
      "id": "10",
      "pais_codigo": "HR",
      "pais_nombre": "Croatia"
    },
    {
      "densidad_poblacion": 198.6,
      "id": "11",
      "pais_codigo": "IT",
      "pais_nombre": "Italy"
    },
    {
      "densidad_poblacion": 97.7,
      "id": "12",
      "pais_codigo": "CY",
      "pais_nombre": "Cyprus"
    },
    {
      "densidad_poblacion": 29.8,
      "id": "13",
      "pais_codigo": "LV",
      "pais_nombre": "Latvia"
    },
    {
      "densidad_poblacion": 44.7,
      "id": "14",
      "pais_codigo": "LT",
      "pais_nombre": "Lithuania"
    },
    {
      "densidad_poblacion": 247.5,
      "id": "15",
      "pais_codigo": "LU",
      "pais_nombre": "Luxembourg"
    },
    {
      "densidad_poblacion": 106.4,
      "id": "16",
      "pais_codigo": "HU",
      "pais_nombre": "Hungary"
    },
    {
      "densidad_poblacion": 1656.7,
      "id": "17",
      "pais_codigo": "MT",
      "pais_nombre": "Malta"
    },
    {
      "densidad_poblacion": 512.8,
      "id": "18",
      "pais_codigo": "NL",
      "pais_nombre": "Netherlands"
    },
    {
      "densidad_poblacion": 108.5,
      "id": "19",
      "pais_codigo": "AT",
      "pais_nombre": "Austria"
    },
    {
      "densidad_poblacion": 122.9,
      "id": "20",
      "pais_codigo": "PL",
      "pais_nombre": "Poland"
    },
    {
      "densidad_poblacion": 113.9,
      "id": "21",
      "pais_codigo": "PT",
      "pais_nombre": "Portugal"
    },
    {
      "densidad_poblacion": 81.6,
      "id": "22",
      "pais_codigo": "RO",
      "pais_nombre": "Romania"
    },
    {
      "densidad_poblacion": 104.6,
      "id": "23",
      "pais_codigo": "SI",
      "pais_nombre": "Slovenia"
    },
    {
      "densidad_poblacion": 111.8,
      "id": "24",
      "pais_codigo": "SK",
      "pais_nombre": "Slovakia"
    },
    {
      "densidad_poblacion": 18.2,
      "id": "25",
      "pais_codigo": "FI",
      "pais_nombre": "Finland"
    },
    {
      "densidad_poblacion": 25.6,
      "id": "26",
      "pais_codigo": "SE",
      "pais_nombre": "Sweden"
    },
    {
      "densidad_poblacion": 3.7,
      "id": "27",
      "pais_codigo": "IS",
      "pais_nombre": "Iceland"
    },
    {
      "densidad_poblacion": 248.0,
      "id": "28",
      "pais_codigo": "LI",
      "pais_nombre": "Liechtenstein"
    },
    {
      "densidad_poblacion": 14.8,
      "id": "29",
      "pais_codigo": "NO",
      "pais_nombre": "Norway"
    },
    {
      "densidad_poblacion": 218.4,
      "id": "30",
      "pais_codigo": "CH",
      "pais_nombre": "Switzerland"
    },
    {
      "densidad_poblacion": 45.5,
      "id": "32",
      "pais_codigo": "ME",
      "pais_nombre": "Montenegro"
    },
    {
      "densidad_poblacion": 78.4,
      "id": "33",
      "pais_codigo": "MK",
      "pais_nombre": "North Macedonia"
    },
    {
      "densidad_poblacion": 100.0,
      "id": "34",
      "pais_codigo": "AL",
      "pais_nombre": "Albania"
    }
  ]
}

# Cargar datos geoespaciales (por ejemplo, un archivo shapefile)
world = gpd.read_file('coords.geojson')

# Crear un DataFrame con los datos
df = gpd.GeoDataFrame(datos['datos'], columns=['densidad_poblacion', 'id', 'pais_codigo', 'pais_nombre'])

# Fusionar datos geoespaciales con datos de densidad de población
world = world.merge(df, how='left', left_on='NUTS_ID', right_on='pais_codigo')

# Visualizar los primeros registros de los datos
print(world.head())

# Crear un mapa cloroplético
world.plot(column='densidad_poblacion',  # Columna que se utilizará para la codificación de color
           cmap='OrRd',        # Mapa de colores (puedes cambiarlo según tus preferencias)
           legend=True,        # Mostrar la leyenda
           legend_kwds={'label': "Población por país"})  # Etiqueta de la leyenda

plt.show()