import requests

# URL del servicio
url = "http://localhost:1026/v2/entities/AirQualityUnit01"

# Realizar la solicitud GET
response = requests.get(url)

# Imprimir la respuesta del servidor
print(response.status_code)
print(response.text)

