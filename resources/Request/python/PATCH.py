import requests
import json
import time
import random

# URL del servicio
url = "http://localhost:1026/v2/entities/AirQualityUnit01/attrs"

# Cabeceras de la solicitud
headers = {
    "Content-Type": "application/json"
}

# Datos a enviar en la solicitud PATCH
payload = {
    "CO": {
        "value": 63,
        "type": "Number"
    }
}

for i in range(50):

    # Valor aleatorio del CO
    valor = random.randint(20, 60)

    # cambio del valor en el JSON
    payload["CO"]["value"] = valor

    # Convertir el diccionario a formato JSON
    payload_json = json.dumps(payload)

    # Realizar la solicitud PATCH
    response = requests.patch(url, headers=headers, data=payload_json)

    # Imprimir la respuesta del servidor
    print(response.status_code)
    print(response.text)
    
    # Pausa 10 seg el programa
    time.sleep(10)

