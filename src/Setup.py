#!/usr/bin/env python3

import json
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def create_default_entity_payload(name: str, latitude: float, longitude: float) -> dict:
    return {
        "id": name,
        "type": "CalidadAgua",
        "dateObserved": {
            "type": "DateTime",
            "value": datetime.now().isoformat()
        },
        "location": {
            "value": {
                "type": "Point",
                "coordinates": [latitude, longitude]
            },
            "type": "geo:json"
        },
        "temperature": {
            "type": "Number",
            "value": "22.5"
        },
        "ph": {
            "type": "Number",
            "value": "6.9"
        },
        "turbidity": {
            "type": "Number",
            "value": "0.7"
        },
        "conductivity": {
            "type": "Number",
            "value": "0.2"
        },
        "level": {
            "type": "Number",
            "value": "4.2"
        },
        "chlorine": {
            "type": "Number",
            "value": "0.3"
        }
    }


def create_quantum_leap_subscription_payload() -> dict:
    return {
        "description": "QuantumLeap subscription to 'CalidadAgua' entities",
        "subject": {
            "entities": [
                {
                    "idPattern": ".*",
                    "type": "CalidadAgua"
                }
            ],
            "condition": {
                "attrs": [
                    "chlorine",
                    "conductivity",
                    "level",
                    "ph",
                    "turbidity",
                    "temperature"
                ]
            }
        },
        "notification": {
            "attrs": [
                "id",
                "type",
                "chlorine",
                "conductivity",
                "level",
                "ph",
                "turbidity",
                "temperature",
                "location"
            ],
            "http": {
                "url": "{{quantumleap}}/v2/notify"
            },
            "metadata": [
                "dateCreated",
                "dateModified"
            ]
        }
    }


# Server URL
url_entity = f"{os.getenv("HOST_ORION")}/v2/entities"
url_subscription = f"{os.getenv("HOST_ORION")}/v2/subscriptions"

# Request headers
headers = {
    "Content-Type": "application/json"
}

# Create first entity
first_entity_payload = json.dumps(
    create_default_entity_payload("JulianSanchez_01", 28.68067302552239, -17.952855018757607)
)
first_entity_response = requests.post(url_entity, headers=headers, data=first_entity_payload)

# Create second entity
second_entity_payload = json.dumps(
    create_default_entity_payload("JulianSanchez_02", 28.805544, -17.780556)
)
second_entity_response = requests.post(url_entity, headers=headers, data=second_entity_payload)

# Create QuantumLeap subscription
quantum_leap_subscription_payload = json.dumps(create_quantum_leap_subscription_payload())
quantum_leap_subscription_response = requests.post(url_subscription, headers=headers,
                                                   data=quantum_leap_subscription_payload)
