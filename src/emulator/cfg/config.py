from datetime import datetime

ENTITIES_IDS = ["Vicario", "Barlovento"]

ENTITY_PROPERTIES = {
    "temperature": {
        "type": "Number",
        "value_range": [0, 35]
    },
    "ph": {
        "type": "Number",
        "value_range": [6, 9]
    },
    "turbidity": {
        "type": "Number",
        "value_range": [0, 100]
    },
    "conductivity": {
        "type": "Number",
        "value_range": [50, 1_500]
    },
    "water_lvl": {
        "type": "Number",
        "value_range": [0, 10]
    },
    "chlorine": {
        "type": "Number",
        "value_range": [0, 1]
    }
}

# start and end datetimes to generate messages
DATE_START = datetime(2024, 5, 1)
DATE_END = datetime(2024, 7, 1)

# Periodicity of messages (in seconds)
MESSAGE_PERIOD = 3_600
