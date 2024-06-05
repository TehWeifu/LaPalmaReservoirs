import requests
import json

# URL del endpoint para la suscripción
url = "http://localhost:1026/v2/subscriptions"

# Cabeceras de la solicitud
headers = {
    "Content-Type": "application/json"
}

# Cuerpo de la solicitud
payload = {
    "description": "Suscripcion QuantumLeap AirQuality",
    "subject": {
        "entities": [
            {
                "idPattern": ".*",
                "type": "AirQualityObserved"
            }
        ],
        "condition": {
            "attrs": [
                "CO", "O3", "PM10", "SO2", "NO2", "temperature", "relativeHumidity", "dateobserved"
            ]
        }
    },
    "notification": {
        "attrs": [
            "id", "CO", "O3", "PM10", "SO2", "NO2", "temperature", "relativeHumidity", "dateobserved", "address", "location"
        ],
        "http": {
            "url": "http://quantumleap:8668/v2/notify"
        },
        "metadata": [
            "dateCreated", "dateModified"
        ]
    }
}

# Convertir el cuerpo a formato JSON
payload_json = json.dumps(payload)

# Realizar la solicitud POST
response = requests.post(url, headers=headers, data=payload_json)

# Imprimir la respuesta del servidor
print(response.status_code)
print(response.text)

