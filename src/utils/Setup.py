#!/usr/bin/env python3

import json
import os
from datetime import datetime

import mysql.connector
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def create_default_entity_payload(name: str, latitude: float, longitude: float) -> dict:
    return {
        "id": name,
        "type": "WaterQuality",
        "dateobserved": {
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
            "value": 22.5
        },
        "ph": {
            "type": "Number",
            "value": 7.1
        },
        "turbidity": {
            "type": "Number",
            "value": 80
        },
        "conductivity": {
            "type": "Number",
            "value": 600
        },
        "level": {
            "type": "Number",
            "value": 4.2
        },
        "chlorine": {
            "type": "Number",
            "value": 0.3
        }
    }


def create_quantum_leap_subscription_payload() -> dict:
    return {
        "description": "QuantumLeap subscription to WaterQuality entities",
        "subject": {
            "entities": [
                {
                    "idPattern": ".*",
                    "type": "WaterQuality"
                }
            ],
            "condition": {
                "attrs": [
                    "dateobserved",
                    "temperature",
                    "ph",
                    "turbidity",
                    "conductivity",
                    "level",
                    "chlorine",
                ]
            }
        },
        "notification": {
            "attrs": [
                "id",
                "type",
                "location",
                "dateobserved",
                "temperature",
                "ph",
                "turbidity",
                "conductivity",
                "level",
                "chlorine"
            ],
            "http": {
                "url": f"{os.getenv("HOST_QUANTUMLEAP")}/v2/notify"
            },
            "metadata": [
                "dateCreated",
                "dateModified"
            ]
        }
    }


def create_data_warehouse_database():
    conn = mysql.connector.connect(
        host=os.getenv('DATA_WAREHOUSE_DB_HOST'),
        user=os.getenv('DATA_WAREHOUSE_DB_USER'),
        password=os.getenv('DATA_WAREHOUSE_DB_PASSWORD'),
        database=os.getenv('DATA_WAREHOUSE_DB_DATABASE')
    )

    cursor = conn.cursor()

    query_create_buoys = ("CREATE TABLE `buoys` ("
                          "`entity`    VARCHAR(50),"
                          "`latitude`  FLOAT,"
                          "`longitude` FLOAT,"
                          "PRIMARY KEY (`entity`)"
                          ")")
    cursor.execute(query_create_buoys)

    query_create_aggregated = ("CREATE TABLE `buoy_hourly_aggregates` ("
                               "`entity` VARCHAR(255),"
                               "`date_observed` DATETIME,"
                               "`property` VARCHAR(255),"
                               "`avg_value` FLOAT,"
                               "`min_value` FLOAT,"
                               "`max_value` FLOAT"
                               ")")
    cursor.execute(query_create_aggregated)

    cursor.close()
    conn.close()


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

# Create Data Warehouse database
create_data_warehouse_database()
