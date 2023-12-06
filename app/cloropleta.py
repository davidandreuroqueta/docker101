from flask import Flask, send_file
import requests
import json
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from mpl_toolkits.axes_grid1 import make_axes_locatable

def get_data(ip, port, endpoint):
    url = f'http://{ip}:{port}/{endpoint}'
    resp = requests.get(url)
    print(resp.text)
    j = json.loads(resp.text)
    return dict(j)

def graph(ip, port, endpoint):
    datos = get_data(ip, port, endpoint)

    # Cargar datos geoespaciales (por ejemplo, un archivo shapefile)
    world = gpd.read_file('coords.geojson')

    # Crear un DataFrame con los datos
    df = gpd.GeoDataFrame(datos['datos'], columns=['densidad_poblacion', 'id', 'pais_codigo', 'pais_nombre'])

    # Fusionar datos geoespaciales con datos de densidad de población
    world = world.merge(df, how='left', left_on='NUTS_ID', right_on='pais_codigo')

    # Visualizar los primeros registros de los datos
    print(world.head())

    # Crear un choropleth map más estilizado con Matplotlib
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)

    # Usar colores más atractivos y agregar una barra de color
    world.plot(column='densidad_poblacion', cmap='YlGnBu', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, cax=cax)
    ax.set_title('Densidad de población en Europa', fontsize=16)
    ax.set_axis_off()  # Ocultar ejes

    # Añadir un título y ajustar el diseño
    plt.tight_layout()
    
    file_dir = './cloropleta.png'
    plt.savefig(file_dir, format='png')
    
    return file_dir

app = Flask(__name__)

@app.route('/plot', methods=['GET'])
def get_plot():
    ip, port, endpoint = 'api', '5000', 'data'
    graph_dir = graph(ip, port, endpoint)
    return send_file(graph_dir)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)