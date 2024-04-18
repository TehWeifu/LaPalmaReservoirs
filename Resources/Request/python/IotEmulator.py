import json
import time

import requests

# URL of the service
url = "http://localhost:1026/v2/entities"

# Headers of the request
headers = {
    "Content-Type": "application/json"
}

# Data to send in the POST request
payload = {
    "id": "AirQualityUnit01",
    "type": "AirQualityObserved",
    "dateObserved": {
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

# Convert the dictionary to JSON format
payload_json = json.dumps(payload)

# Time interval (in seconds)
seconds = 5

while True:
    # Make the POST request
    response = requests.post(url, headers=headers, data=payload_json)

    # Print the server response
    print(response.status_code)
    print(response.text)

    # Wait for x seconds
    time.sleep(seconds)
