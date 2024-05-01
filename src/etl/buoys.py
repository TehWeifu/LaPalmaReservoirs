import os

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


# Fetch data from CrateDB
buoys = fetch_data()
df_buoy = pd.DataFrame(
    buoys,
    columns=["entity", "latitude", "longitude"]
)

# Save the DataFrame to a CSV file
df_buoy.to_csv("./../../data/buoys.csv", index=False)
