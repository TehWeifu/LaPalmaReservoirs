import requests
import json

# URL del servicio
url = "http://localhost:1026/v2/entities"

# Cabeceras de la solicitud
headers = {
    "Content-Type": "application/json"
}

# Datos a enviar en la solicitud POST
payload = {
    "id": "AirQualityUnit01",
    "type": "AirQualityObserved",
    "dateobserved": {
        "type": "DateTime",
        "value": "2018-07-30T18:00:00-05:00"
    },
    "address": {
        "type": "StructuredValue",
        "value": {
            "addressCountry": "MX",
            "addressLocality": "Ciudad de Mexico",
            "streetAddress": "Centro"
        }
    },
    "location": {
        "value": {
            "type": "Point",
            "coordinates": [28.68067302552239, -17.952855018757607]
        },
        "type": "geo:json"
    },
    "source": {
        "type": "Text",
        "value": "http://www.aire.cdmx.gob.mx/"
    },
    "temperature": {
        "type": "Number",
        "value": "0"
    },
    "relativeHumidity": {
        "type": "Number",
        "value": "0"
    },
    "CO": {
        "type": "Number",
        "value": "0"
    },
    "O3": {
        "type": "Number",
        "value": "0"
    },
    "NO2": {
        "type": "Number",
        "value": "0"
    },
    "SO2": {
        "type": "Number",
        "value": "0"
    },
    "PM10": {
        "type": "Number",
        "value": "0"
    }
}

# Convertir el diccionario a formato JSON
payload_json = json.dumps(payload)

# Realizar la solicitud POST
response = requests.post(url, headers=headers, data=payload_json)

# Imprimir la respuesta del servidor
print(response.status_code)
print(response.text)
