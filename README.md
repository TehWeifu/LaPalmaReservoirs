# Scripts

- Setup: initializes two entities in Orion Context Broker and a subscription to QuantumLeap

# Environment Variables

This project uses the following environment variables (default values are provided in the `.env` file):

- `HOST_ORION`: IP address of the Orion Context Broker
- `HOST_QUANTUMLEAP`: IP address of the QuantumLeap server
- `HOST_CRATE`: IP address of the CrateDB server

# Useful Commands

Initialize architecture: `docker-compose -f docker-compose_SDD.yml up -d`
Stop architecture: `docker-compose -f docker-compose_SDD.yml down`

# Endpoints

- Local (VM):
    - Orion: `http://192.168.56.104:1026`
    - QuantumLeap: `http://192.168.56.104:8668`
    - Grafana: `http://192.168.56.104:3000`
    - Crate: `http://192.168.56.104:4200/#!/`
- Remote (server):
    - Orion: `http://orion.lapalma.fpmislata.es`
    - QuantumLeap: `http://orion.lapalma.fpmislata.es:8668`
    - Grafana: `http://orion.lapalma.fpmislata.es:3000`
    - Crate: `http://orion.lapalma.fpmislata.es:4200/#!/`

# Grafana

Steps to add CrateDB as Grafana data source:

* Host: crate:5432
* Database: doc
* Username: crate
* Password: *empty*
* TLS/SSL Mode: disable
* PostgreSQL Version: 9.3
