# Scripts

- Setup: initializes two entities in Orion Context Broker and a subscription to QuantumLeap

# Environment Variables

This project uses the following environment variables (default values are provided in the `.env` file):

- `HOST_ORION`: IP address of the Orion Context Broker

# Useful Commands

Initialize architecture: `docker-compose -f docker-compose_SDD.yml up -d`
Stop architecture: `docker-compose -f docker-compose_SDD.yml down`

# Endpoints

- Local (VM):
    - Orion: `http://192.168.56.102:1026`
    - QuantumLeap: `http://192.168.56.102:8668`
- Remote (server):
    - Orion: `http://orion.lapalma.fpmislata.es`
    - QuantumLeap: `http://orion.lapalma.fpmislata.es:8668`
