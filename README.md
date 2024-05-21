# Scripts

- emulator
    - BuoyEmulator: simulates the behavior of a buoy (according to parameters in config file)
- etl
    - aggregation: fetch data from Crate and transforms it into a format for PowerBI
    - buoys: fetch the different buoys from the database and load them into a .csv file
- utils
    - Setup: initializes two entities in Orion Context Broker and a subscription to QuantumLeap

# Environment Variables

This project uses the following environment variables (default values are provided in the `.env` file):

- `HOST_ORION`: IP address of the Orion Context Broker
- `HOST_QUANTUMLEAP`: IP address of the QuantumLeap server
- `HOST_CRATE`: IP address of the CrateDB server

- `DATA_WAREHOUSE_DB_HOST`: IP address of the MySql server for the data warehouse
- `DATA_WAREHOUSE_DB_USER`: username for the MySql server
- `DATA_WAREHOUSE_DB_PASSWORD`: password for the MySql server
- `DATA_WAREHOUSE_DB_DATABASE`: name of the database in the MySql server

# Docker

Initialize architecture: `docker-compose -f docker-compose_SDD.yml up -d`
Stop architecture: `docker-compose -f docker-compose_SDD.yml down`

Note: sometimes the Orion container does not start correctly and crashes as soon as it starts. In that case, delete the
log file and restart the architecture.
`cd /var/lib/docker/containers/<container_id>/`
`sudo rm <container_id>-json.log`

# Endpoints

- Local (VM):
    - Orion: `http://192.168.56.102:1026`
    - QuantumLeap: `http://192.168.56.102:8668`
    - Grafana: `http://192.168.56.102:3000`
    - Crate: `http://192.168.56.102:4200/#!/`
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

# SQLs

CREATE DATABASE LaPalmaReservoirs;
USE LaPalmaReservoirs;

CREATE TABLE `buoy_hourly_aggregates`
(
`entity`        VARCHAR(50),
`date_observed` DATE,
`property`      VARCHAR(50),
`avg_value`     FLOAT,
`min_value`     FLOAT,
`max_value`     FLOAT,
PRIMARY KEY (`entity`, `date_observed`, `property`)
)

CREATE TABLE `buoys`
(
`entity`    VARCHAR(50),
`latitude`  FLOAT,
`longitude` FLOAT,
PRIMARY KEY (`entity`)
)
