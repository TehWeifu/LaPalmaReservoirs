import os

import mysql.connector
import pandas as pd
from crate import client
from dotenv import load_dotenv

load_dotenv()


def fetch_data() -> list:
    connection = client.connect(os.getenv("HOST_CRATE"), username="crate", password=None, timeout=10)
    cursor = connection.cursor()

    query = ("SELECT "
             "entity_id, dateobserved, temperature, ph, turbidity, conductivity, level, chlorine "
             "FROM etwaterquality")

    try:
        cursor.execute(query)
        # Fetch all with column names
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print("An error occurred:", e)
    finally:
        cursor.close()
        connection.close()


def load_to_csv(aggregated_data: pd.DataFrame):
    # Save the DataFrame to a CSV file
    aggregated_data.to_csv("./../../data/etwaterquality.csv", index=False)


def load_to_database(aggregated_data: pd.DataFrame):
    # Save the DataFrame to a MySQL database
    conn = mysql.connector.connect(
        host=os.getenv('DATA_WAREHOUSE_DB_HOST'),
        user=os.getenv('DATA_WAREHOUSE_DB_USER'),
        password=os.getenv('DATA_WAREHOUSE_DB_PASSWORD'),
        database=os.getenv('DATA_WAREHOUSE_DB_DATABASE')
    )

    cursor = conn.cursor()

    insert_query = ("INSERT INTO `buoy_hourly_aggregates` "
                    "(entity, date_observed, property, avg_value, min_value, max_value) "
                    "VALUES (%s, %s, %s, %s, %s, %s)")

    data_to_insert = list(aggregated_data.itertuples(index=False, name=None))
    cursor.executemany(insert_query, data_to_insert)

    conn.commit()

    cursor.close()
    conn.close()


# Fetch data from CrateDB
data_fetched = fetch_data()
df_buoy = pd.DataFrame(
    data_fetched,
    columns=["entity", "date_observed", "temperature", "ph", "turbidity", "conductivity", "level",
             "chlorine"]
)

# Unpivot the DataFrame
df_buoy = pd.melt(
    df_buoy,
    id_vars=["entity", "date_observed"],
    value_vars=["temperature", "ph", "turbidity", "conductivity", "level", "chlorine"],
    var_name="property",
    value_name="value"
)

# Convert the date_observed to only keep the date part
df_buoy["date_observed"] = pd.to_datetime(df_buoy["date_observed"], unit="ms")
df_buoy["date_observed"] = df_buoy["date_observed"].dt.strftime("%Y-%m-%d")

# Group by entity, date_observed, and property, and calculate the average, min, and max values
df_buoy = df_buoy.groupby(["entity", "date_observed", "property"]).agg(
    avg_value=("value", "mean"),
    min_value=("value", "min"),
    max_value=("value", "max")
).reset_index()

load_to_csv(df_buoy)
load_to_database(df_buoy)
