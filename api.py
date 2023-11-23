from flask import Flask
import requests
import json

app = Flask(__name__)

def get_density():
    # URL del punto final de la API de Eurostat
    eurostat_api_url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"

    def eurostat_api_request(dataset_code, filters=None, format="JSON"):
        """
        Realiza una solicitud a la API de Eurostat y recupera datos.

        Parámetros:
        - dataset_code: El código del conjunto de datos que deseas recuperar.
        - filters: Filtros opcionales para reducir los datos. (por ejemplo, {'geo': 'DE', 'time': '2020'})
        - format: El formato en el que se deben devolver los datos. El valor predeterminado es JSON.

        Retorna:
        - Un diccionario que contiene los datos recuperados.
        """
        # Construir la URL de la solicitud
        request_url = f"{eurostat_api_url}/{dataset_code}"
        
        # Agregar el formato a la solicitud
        request_url += f"?format={format}"

        # Agregar filtros a la solicitud si se proporcionan
        if filters:
            for k, v in filters.items():
                request_url += f"&{k}={v}"
        
        # Agregar geoLevel para que nos devuelva los datos solo por paises
        request_url += "&geoLevel=country"
        
        # Realizar la solicitud
        response = requests.get(request_url)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None

    dataset_code = "DEMO_R_D3DENS"
    filters = {'time': '2022'}
    result = eurostat_api_request(dataset_code, filters)
    return result

def transform(data):
    # Convertir el diccionario a un DataFrame de Pandas
    d = dict(data)
    values = d["value"]
    ids = d["dimension"]["geo"]["category"]["index"]
    label = d["dimension"]["geo"]["category"]["label"]

    rows = []
    for k, v in ids.items():
        try:
            densidad_poblacion = values[str(v)]
        except Exception as e:
            continue
        pais_nombre = label[k]
        row = {'id': str(v), 'pais_codigo': k, 'pais_nombre': pais_nombre, 'densidad_poblacion': densidad_poblacion}
        rows.append(row)

    data = {'datos': rows}
    return data


@app.route('/data')
def hola():
    raw_data = get_density()
    data = transform(raw_data)
    return data

if __name__ == '__main__':
    app.run(debug=True)