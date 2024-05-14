import os

import mysql.connector
import pandas as pd
from crate import client
from dotenv import load_dotenv

load_dotenv()


def fetch_data():
    connection = client.connect(os.getenv("HOST_CRATE"), username="crate", password=None, timeout=10)
    cursor = connection.cursor()

    query = ("SELECT entity_id, "
             "MAX(longitude(location_centroid)) AS latitude, "
             "MAX(latitude(location_centroid)) AS longitude "
             "FROM etwaterquality "
             "GROUP BY entity_id;")

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


def load_to_csv(buoys: pd.DataFrame):
    # Save the DataFrame to a CSV file
    buoys.to_csv("./../../data/buoys.csv", index=False)


def load_to_database(buoys: pd.DataFrame):
    # Save the DataFrame to a MySQL database

    conn = mysql.connector.connect(
        host=os.getenv('DATA_WAREHOUSE_DB_HOST'),
        user=os.getenv('DATA_WAREHOUSE_DB_USER'),
        password=os.getenv('DATA_WAREHOUSE_DB_PASSWORD'),
        database=os.getenv('DATA_WAREHOUSE_DB_DATABASE')
    )

    cursor = conn.cursor()

    insert_query = ("INSERT INTO `buoys` "
                    "(entity, latitude, longitude) "
                    "VALUES (%s, %s, %s)")

    data_to_insert = list(buoys.itertuples(index=False, name=None))
    cursor.executemany(insert_query, data_to_insert)

    conn.commit()

    cursor.close()
    conn.close()


# Fetch data from CrateDB
buoys_fetched = fetch_data()
df_buoy = pd.DataFrame(
    buoys_fetched,
    columns=["entity", "latitude", "longitude"]
)

load_to_csv(df_buoy)
load_to_database(df_buoy)
