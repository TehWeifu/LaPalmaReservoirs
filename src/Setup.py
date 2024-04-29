#!/usr/bin/env python3

import json

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def create_default_entity_payload(name: str) -> dict:
    return {
        "id": name,
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


# Server URL
url = "http://localhost:1026/v2/entities"

# Request headers
headers = {
    "Content-Type": "application/json"
}

# Create first entity
first_entity_payload = json.dumps(create_default_entity_payload("JulianSanchez_01"))
first_entity_response = requests.post(url, headers=headers, data=first_entity_payload)

# Create second entity
second_entity_payload = json.dumps(create_default_entity_payload("JulianSanchez_01"))
second_entity_response = requests.post(url, headers=headers, data=second_entity_payload)
