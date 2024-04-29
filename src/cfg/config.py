from datetime import datetime

ENTITIES_IDS = ["JulianSanchez_01", "JulianSanchez_02"]

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
    "level": {
        "type": "Number",
        "value_range": [0, 10]
    },
    "chlorine": {
        "type": "Number",
        "value_range": [0, 1]
    }
}

# Start and End Dates for Message Generation
DATE_START = datetime(2024, 4, 1)
DATE_END = datetime(2024, 4, 2)

# Periodicity of messages (in seconds)
MESSAGE_PERIOD = 10
