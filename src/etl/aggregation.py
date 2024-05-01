import os

import pandas as pd
from crate import client
from dotenv import load_dotenv

load_dotenv()


def fetch_data():
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

# Save the DataFrame to a CSV file
df_buoy.to_csv("./../../data/etwaterquality.csv", index=False)
