#!/usr/bin/env python3

import logging
import os
import random
import sys
from datetime import timedelta
from logging import Logger

import requests
from dotenv import load_dotenv

from src.cfg.config import *

load_dotenv()

# URL of the service
url = f"{os.getenv("HOST_ORION")}/v2/entities"

# Headers of the request
headers = {
    "Content-Type": "application/json"
}


def initialize_logger(name: str) -> Logger:
    logging.basicConfig(level=logging.DEBUG)
    logger = Logger(name)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


def fetch_entities(entity_names: list) -> list:
    entities_fetched = []
    for entity_name in entity_names:
        my_url = f"{url}/{entity_name}"
        response = requests.get(my_url)
        entities_fetched.append(response.json())
    return entities_fetched


def calculate_property_random_value(entity: dict, key: str) -> dict:
    current_value = float(entity[key]["value"])  # Get the current value of the property

    value_range = ENTITY_PROPERTIES[random_key_chosen]["value_range"]  # Get the range of the property

    delta = random.uniform(value_range[0], value_range[1]) * random.uniform(-.1, .1)  # Modify the value by +-10%

    new_value = current_value + delta
    new_value = max(value_range[0], min(value_range[1], new_value))  # Clamp the value to the range

    return new_value


logger = initialize_logger("buoy_emulator")

entities = fetch_entities(ENTITIES_IDS)

DATE_ITERATOR = DATE_START
while DATE_ITERATOR < DATE_END:

    for entity in entities:
        # Payload
        payload = {
            "id": entity["id"],
            "type": entity["type"],
            "dateObserved": {
                "type": "DateTime",
                "value": DATE_ITERATOR.isoformat()
            }
        }

        # Pick a random property to be updated
        random_key_chosen = random.choice(list(ENTITY_PROPERTIES.keys()))

        # Calculate the new value for the property
        random_value = calculate_property_random_value(entity, random_key_chosen)
        payload[random_key_chosen] = {
            "type": ENTITY_PROPERTIES[random_key_chosen]["type"],
            "value": random_value
        }

        # Send the POST request
        response = requests.patch(url, headers=headers, json=payload)

        logger.debug(
            f"Entity: {entity['id']} - Property: {random_key_chosen} - Value: {random_value} - Date: {DATE_ITERATOR} - Response: {response.status_code}"
        )

    DATE_ITERATOR += timedelta(seconds=MESSAGE_PERIOD)
